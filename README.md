# 🏠 House Price Prediction API

A Machine Learning-based REST API that predicts house prices using property features such as city, location, property type, area, and amenities.

The project is built with **Python**, **FastAPI**, and **Scikit-learn**, providing accurate house price predictions through a simple API.

---

# 📌 Features

- Predict house prices using a trained Machine Learning model.
- FastAPI REST API for real-time predictions.
- Automatic interactive API documentation (Swagger UI).
- Loads a pre-trained model using Joblib.
- Handles categorical feature encoding.
- Returns prediction results in JSON format.

---

# 🛠️ Technologies Used

### Programming Language
- Python 3

### Machine Learning
- Scikit-learn
- Pandas
- NumPy
- Joblib

### Backend
- FastAPI
- Uvicorn

---

# 📂 Project Structure

```text
House-Price-Prediction/
│
├── Dataset/
│   ├── description.json
│   ├── inquiries.json
│   └── properties.json
│
├── price_predictor/
│   ├── app.py
│   ├── model.ipynb
│   ├── price_model.pkl
│   ├── model_columns.pkl
│   ├── city_list.pkl
│   ├── location_list.pkl
│   ├── amenity_list.pkl
│   ├── type_list.pkl
│   ├── requirements.txt
│   └── __pycache__/
│
├── .gitignore
└── README.md
```

---

# ⚙️ Installation

## 1. Clone the repository

```bash
git clone https://github.com/TufailAbbas/Real-Estate-AI-Backend
```

Replace **YOUR_USERNAME** and **YOUR_REPOSITORY** with your actual GitHub username and repository name.

---

## 2. Navigate to the project

```bash
cd House-Price-Prediction
```

---

## 3. Install the required packages

```bash
python -m pip install -r price_predictor/requirements.txt
```

---

# ▶️ Run the API

Start the FastAPI server:

```bash
python -m uvicorn price_predictor.app:app --reload
```

After the server starts, open:

### API

```
http://127.0.0.1:8000
```

### Swagger Documentation

```
http://127.0.0.1:8000/docs
```

Swagger allows you to test every endpoint directly from your browser.

---

# 📊 Machine Learning Workflow

The prediction model was developed using the following pipeline:

1. Load dataset
2. Data preprocessing
3. Handle missing values
4. Encode categorical features
5. Feature selection
6. Train-Test Split
7. Train Linear Regression model
8. Evaluate model performance
9. Save model using Joblib
10. Deploy model using FastAPI

---

# 📁 Model Files

The following files are used during prediction:

| File | Description |
|------|-------------|
| `price_model.pkl` | Trained Machine Learning model |
| `model_columns.pkl` | Input feature names |
| `city_list.pkl` | List of supported cities |
| `location_list.pkl` | List of supported locations |
| `amenity_list.pkl` | List of amenities |
| `type_list.pkl` | List of property types |

---

# 🚀 API Response

The API returns the predicted house price as JSON.

Example response:

```json
{
    "predicted_price": 15250000
}
```

---

# 🧪 Testing the API

You can test the API in two ways:

- Swagger UI
- REST clients such as Postman

Swagger URL:

```
http://127.0.0.1:8000/docs
```

---

# 🔮 Future Improvements

- Develop a responsive web frontend.
- Improve prediction accuracy using advanced ML models.
- Deploy the application to the cloud.
- Store prediction history in a database.
- Add authentication and user management.
- Support image-based property analysis.

---

# 👨‍💻 Author

**Tufail Abbas**

Computer Science Student

University of Peshawar

Interested in:
- Artificial Intelligence
- Machine Learning
- Deep Learning
- FastAPI
- Backend Development

---

# 📄 License

This project is intended for educational and learning purposes.