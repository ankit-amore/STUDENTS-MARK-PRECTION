# Student Marks Prediction App

A simple Machine Learning web application built using Flask that predicts student marks based on study hours.

---

# Project Overview

This application uses a trained Machine Learning model to predict the percentage of marks a student may score depending on the number of study hours entered by the user.

The app:
- Accepts study hours from the user
- Predicts marks using a trained model
- Displays the predicted result
- Saves prediction history into a CSV file

---

# Technologies Used

- Python
- Flask
- NumPy
- Pandas
- Scikit-learn
- HTML

---

# Project Structure

```bash
project/
│
├── app.py
├── Desktop.plk
├── smp_data_from_app.csv
│
├── templates/
│   └── index.html
│
├── static/
│   └── style.css
│
└── README.md
```

---

# Installation

## 1. Clone the Repository

```bash
git clone <your-github-repo-url>
```

---

## 2. Navigate to Project Folder

```bash
cd project-name
```

---

## 3. Create Virtual Environment (Optional)

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux/Mac

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 4. Install Dependencies

```bash
pip install flask numpy pandas scikit-learn joblib
```

Or use:

```bash
pip install -r requirements.txt
```

---

# Running the Application

Run the Flask application:

```bash
python app.py
```

Server will start at:

```bash
http://127.0.0.1:5000/
```

Open the browser and visit the URL above.

---

# Features

- Predict student marks
- Input validation
- CSV data storage
- Simple Flask web interface
- Real-time predictions

---

# Input Validation

The application validates study hours:

- Minimum Hours: 1
- Maximum Hours: 24

If invalid input is entered, the app displays an error message.

---

# Model Information

The trained model is loaded using:

```python
joblib.load("Desktop.plk")
```

The model predicts marks based on:
- Study Hours

---

# Prediction Flow

1. User enters study hours
2. Flask receives POST request
3. Input converted into NumPy array
4. ML model predicts marks
5. Result displayed on webpage
6. Data saved into CSV file

---

# CSV Storage

Predictions are stored in:

```bash
smp_data_from_app.csv
```

Example:

| Study Hours | Predicted Output |
|---|---|
| 5 | 65.2 |
| 8 | 89.4 |

---

# Example Output

```text
You will get [85.4%] marks when you study [7] hours per day
```

---

# Future Improvements

- Add database support
- Deploy on Heroku/Render
- Add user authentication
- Improve frontend UI
- Add graphs and analytics
- Train advanced ML models

---

# Requirements

Create a `requirements.txt` file:

```txt
flask
numpy
pandas
scikit-learn
joblib
```

Install using:

```bash
pip install -r requirements.txt
```

---
