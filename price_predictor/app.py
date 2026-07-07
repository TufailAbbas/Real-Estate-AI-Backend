"""
Property Price Predictor - FastAPI
------------------------------------
Exposes a prediction API that a Flutter app (or any frontend) can call.

Run locally:
    pip install -r requirements.txt
    uvicorn app:app --host 0.0.0.0 --port 8000 --reload

Then visit http://127.0.0.1:8000/docs to see auto-generated,
interactive API documentation (Swagger UI) - the Flutter dev can
use this to explore/test the API without writing any code first.

Requires these files in the same folder:
    price_model.pkl
    model_columns.pkl
    amenity_list.pkl
    city_list.pkl
    location_list.pkl
    type_list.pkl
"""

import os
from typing import List, Optional

import joblib
import pandas as pd
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def load_pkl(name):
    return joblib.load(os.path.join(BASE_DIR, name))


# ---------- Load model + reference lists once at startup ----------
model = load_pkl("price_model.pkl")
model_columns = load_pkl("model_columns.pkl")
amenity_list = load_pkl("amenity_list.pkl")
city_list = load_pkl("city_list.pkl")
location_list = load_pkl("location_list.pkl")
type_list = load_pkl("type_list.pkl")


# ---------- App setup ----------
app = FastAPI(title="Property Price Predictor API")

# Allows the Flutter app (running on a phone/emulator, different origin)
# to call this API without being blocked by the browser/webview.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


# ---------- Request / response schemas ----------
class PredictRequest(BaseModel):
    size: float = Field(..., example=1800)
    bedrooms: int = Field(..., example=5)
    bathrooms: int = Field(..., example=3)
    city: str = Field(..., example="Lahore")
    location: str = Field(..., example="DHA")
    type: str = Field(..., example="house")
    amenities: Optional[List[str]] = Field(default=[], example=["Garage", "Swimming Pool"])


class PredictResponse(BaseModel):
    predicted_price: float


class OptionsResponse(BaseModel):
    cities: List[str]
    locations: List[str]
    types: List[str]
    amenities: List[str]


# ---------- Helper: build model input row ----------
def build_input_row(data: PredictRequest) -> pd.DataFrame:
    row = pd.DataFrame([[0] * len(model_columns)], columns=model_columns)

    row["size"] = data.size
    row["bedrooms"] = data.bedrooms
    row["bathrooms"] = data.bathrooms

    for prefix, value in [("city_", data.city), ("location_", data.location), ("type_", data.type)]:
        dummy_col = f"{prefix}{value}"
        if dummy_col in row.columns:
            row[dummy_col] = 1

    for feat in data.amenities:
        if feat in row.columns:
            row[feat] = 1

    return row


# ---------- Routes ----------
@app.get("/")
def home():
    return {"status": "ok", "message": "Property Price Predictor API is running"}


@app.get("/options", response_model=OptionsResponse)
def options():
    """Lets the Flutter app fetch valid dropdown values dynamically."""
    return {
        "cities": city_list,
        "locations": location_list,
        "types": type_list,
        "amenities": amenity_list,
    }


@app.post("/predict", response_model=PredictResponse)
def predict(data: PredictRequest):
    try:
        row = build_input_row(data)
        prediction = model.predict(row)[0]
        return {"predicted_price": round(float(prediction), 2)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
