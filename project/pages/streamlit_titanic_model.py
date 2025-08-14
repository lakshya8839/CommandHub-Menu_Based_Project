# pages/Titanic Survival Predictor.py

import streamlit as st
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

st.set_page_config(page_title="Titanic Predictor", layout="centered")
st.title("🚢 Titanic Survival Predictor")

# Load CSV
@st.cache_data
def load_data():
    return pd.read_csv("titanic (1).csv")  

df = load_data()

# Show dataset
if st.checkbox("Show Data"):
    st.dataframe(df)

# Preprocessing
df["Age"].fillna(df["Age"].mean(), inplace=True)
df["Embarked"].fillna(df["Embarked"].mode()[0], inplace=True)
df["Sex"] = df["Sex"].map({"male": 0, "female": 1})
df["Embarked"] = df["Embarked"].map({"S": 0, "C": 1, "Q": 2})

# Features and labels
X = df[["Pclass", "Sex", "Age", "SibSp", "Parch", "Fare", "Embarked"]]
y = df["Survived"]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)

# Train model
model = LogisticRegression(max_iter=200)
model.fit(X_train, y_train)

# Accuracy
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
st.write(f"✅ Model Accuracy: **{accuracy:.2f}**")

# User input
st.header("🎯 Try Predicting Your Survival")

pclass = st.selectbox("Passenger Class", [1, 2, 3])
sex = st.radio("Sex", ["male", "female"])
age = st.slider("Age", 0, 80, 25)
sibsp = st.slider("Siblings/Spouses", 0, 5, 0)
parch = st.slider("Parents/Children", 0, 5, 0)
fare = st.number_input("Fare Paid", 0.0, 300.0, 50.0)
embarked = st.selectbox("Port", ["S", "C", "Q"])

# Encode input
sex_val = 0 if sex == "male" else 1
embarked_val = {"S": 0, "C": 1, "Q": 2}[embarked]

input_data = [[pclass, sex_val, age, sibsp, parch, fare, embarked_val]]

if st.button("Predict"):
    result = model.predict(input_data)[0]
    msg = "🎉 You would have **Survived**!" if result == 1 else "❌ You would **Not have survived.**"
    st.success(msg)
