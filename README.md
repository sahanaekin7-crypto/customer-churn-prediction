# Customer Churn Prediction

## Project Description

This project predicts whether a customer will **churn or stay** using Machine Learning. It uses the Telco Customer Churn dataset and provides an interactive web application built with Streamlit.

## Objective

The main objective of this project is to identify customers who are likely to leave a service based on their personal, account, and service-related information.

## Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Streamlit
* Machine Learning

## Dataset

The project uses the **Telco Customer Churn dataset**, which contains customer information such as:

* Customer demographics
* Contract type
* Internet service
* Payment method
* Monthly charges
* Total charges
* Churn status

## Features

* Predicts whether a customer will churn or stay
* Interactive Streamlit web application
* Customer details input
* Machine Learning-based prediction
* Simple and user-friendly interface

## Model Performance

The Machine Learning model achieved approximately **96% accuracy** during evaluation.

## Project Structure

```text
Customer-Churn-Prediction/
│
├── app.py
├── train_model.py
├── Telco-Customer-Churn.csv
├── requirements.txt
└── README.md
```

## How to Run

### 1. Install Required Libraries

```bash
pip install -r requirements.txt
```

### 2. Run the Application

```bash
python -m streamlit run app.py
```

### 3. Open the Application

After running the command, a local Streamlit link will be displayed in the terminal. Open that link in your browser to use the application.

## Future Improvements

* Improve model performance
* Add more data visualizations
* Deploy the application online
* Display churn probability
* Add recommendations for reducing customer churn

## Project

**Customer Churn Prediction**

Developed using Python, Machine Learning, and Streamlit.
