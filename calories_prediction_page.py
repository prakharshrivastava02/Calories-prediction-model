import streamlit as st
from joblib import dump, load
import numpy as np

def load_model():
    model = load('calories.joblib')
    return model
model = load_model()
def show_predict_page():
    st.title(" Calories Prediction Model")

    st.write("""### We need some information to predict the salary""")

    
    

    gender = st.number_input("Gender , 0 for Male and 1 for female")
    age = st.slider("age",0,100,1)
    height = st.number_input("Heights")
    weights = st.number_input("Weights")
    duration = st.number_input("Workout duration in minute")
    heartrate = st.number_input("Heartrate")
    bodytemperature = st.number_input("Bodytemperature")

    ok = st.button("Calculate Calories Burn")
    if ok:
        features = np.array([[gender,age,height,weights,duration,heartrate,bodytemperature]])
        salary = model.predict(features)
        st.subheader(f"The estimated Calories burn is {salary[0]:.2f} ")