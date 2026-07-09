# 🏠 House Price Prediction API

## Overview

House Price Prediction API is a Machine Learning project that predicts house prices based on property information. The project is built using **Python**, **FastAPI**, and **Scikit-learn**. A trained Linear Regression model is loaded through FastAPI and returns predicted prices via a REST API.

---

## Features

- Predict house prices using a trained Machine Learning model.
- REST API built with FastAPI.
- Automatic API documentation using Swagger UI.
- Loads pre-trained model and preprocessing files.
- Returns predictions in JSON format.

---

## Technologies Used

- Python
- FastAPI
- Uvicorn
- Scikit-learn
- Pandas
- NumPy
- Joblib

---

## Project Structure

```
House-Price-Prediction/
│
├── Dataset/
│   ├── description.json
│   ├── inquiries.json
│   └── properties.json
│
├── price_predictor/
│   ├── app.py
│   ├── price_model.pkl
│   ├── model_columns.pkl
│   ├── city_list.pkl
│   ├── location_list.pkl
│   ├── amenity_list.pkl
│   ├── type_list.pkl
│   ├── model.ipynb
│   └── requirements.txt
│
├── .gitignore
└── README.md
```

---

## Installation

Clone the repository

```bash
git clone https://github.com/your-username/your-repository.git
```

Move into the project folder

```bash
cd your-repository
```

Install the required packages

```bash
pip install -r price_predictor/requirements.txt
```

---

## Running the API

Run the following command inside the **price_predictor** folder:

```bash
uvicorn app:app --reload
```

The API will start at:

```
http://127.0.0.1:8000
```

Swagger API Documentation:

```
http://127.0.0.1:8000/docs
```

---

## Machine Learning Workflow

1. Load the dataset.
2. Clean and preprocess the data.
3. Encode categorical features.
4. Train the Linear Regression model.
5. Save the trained model using Joblib.
6. Load the model in FastAPI.
7. Accept user input through API requests.
8. Return the predicted house price.

---

## Model Files

The project includes the following saved files:

- `price_model.pkl` – Trained Machine Learning model
- `model_columns.pkl` – Feature column names
- `city_list.pkl` – List of supported cities
- `location_list.pkl` – List of supported locations
- `amenity_list.pkl` – List of amenities
- `type_list.pkl` – Property types

---

## API Response

The API accepts house information and returns the predicted price in JSON format.

Example:

```json
{
    "predicted_price": 14500000
}
```

---

## Future Improvements

- Develop a web frontend.
- Improve prediction accuracy using advanced models.
- Deploy the API to the cloud.
- Add authentication.
- Store prediction history.

---

## Author

**Tufail Abbas**

Computer Science Student

Interested in Artificial Intelligence, Machine Learning, and Backend Development.