import streamlit as st
import pandas as pd
import pickle

# Load model and scaler
model = pickle.load(open("clickstream_model.pkl","rb"))
scaler = pickle.load(open("scaler.pkl","rb"))

st.title("🛍️ Clickstream Product Category Prediction")

st.write("Enter session details")

# -------- INPUT FIELDS -------- #

col1, col2 = st.columns(2)

with col1:
    month = st.number_input("Month",1,12,1)
    day = st.number_input("Day",1,31,1)
    order = st.number_input("Order",1)
    country = st.number_input("Country",1)
    page_2_clothing_model = st.number_input("Clothing Model",1)
    colour = st.number_input("Colour",1)

with col2:
    location = st.number_input("Location",1)
    model_photography = st.number_input("Model Photography",1)
    price = st.number_input("Price",1)
    price_2 = st.number_input("Price 2",1)
    page = st.number_input("Page",1)

# -------- PREDICTION -------- #

if st.button("Predict Category"):

    input_data = pd.DataFrame(
        [[month, day, order, country, page_2_clothing_model,
          colour, location, model_photography, price, price_2, page]],
        
        columns=[
            'month',
            'day',
            'order',
            'country',
            'page_2_clothing_model',
            'colour',
            'location',
            'model_photography',
            'price',
            'price_2',
            'page'
        ]
    )

    scaled_input = scaler.transform(input_data)

    prediction = model.predict(scaled_input)

    st.success(f"🎯 Predicted Main Category: {prediction[0]}")