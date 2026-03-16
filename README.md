Clickstream Online Shopping 

Project Overview
This project focuses on predicting the main product category a user visits on an online shopping website using clickstream session data.
Clickstream data records user interactions such as pages visited, product attributes, and browsing behavior during a shopping session.
Using Machine Learning classification algorithms, the model learns patterns in user browsing behavior and predicts the category of the main page visited.
This project demonstrates the complete machine learning workflow, including:

Data preprocessing
Feature selection
Model training
Model evaluation
Model deployment using Streamlit

Problem Statement
E-commerce platforms generate large volumes of clickstream data. Understanding user browsing behavior helps businesses:
Improve product recommendations
Personalize user experience
Optimize website navigation
Increase conversion rates
The goal of this project is to predict the main product category visited by a user during a session using historical clickstream data.

Dataset Information
The dataset contains clickstream information from an online clothing store. Each row represents a user interaction with the website.
Dataset Features
Feature	Description
month	Month of the browsing session
day	Day of the browsing session
order	Order of page visit in the session
country	Country of the visitor
page_2_clothing_model	Clothing model displayed on the second page
colour	Color of the clothing item
location	Location of the product on the webpage
model_photography	Type of product photography
price	Product price category
price_2	Secondary price category
page	Page number visited
Target Variable
Column	Description
page_1_main_category	Main product category visited

Technologies Used
Python
Pandas
NumPy
Scikit-learn
Matplotlib / Seaborn
Streamlit

Machine Learning Workflow
Data Preprocessing
Removed unnecessary columns
Handled missing values
Cleaned column names
Feature scaling using StandardScaler
Feature Selection
The following features were used for training:
month
day
order
country
page_2_clothing_model
colour
location
model_photography
price
price_2
page
Model Training
A classification model was trained to predict the main product category.
Example algorithms used:
Logistic Regression
Random Forest Classifier
Support Vector Machine
Decision Tree
The best-performing model was selected based on accuracy.
Model Evaluation
Evaluation metrics used:
Accuracy
Confusion Matrix
Classification Report

Model Deployment
The trained model was deployed using Streamlit, allowing users to input session details and receive predictions in real time.
Streamlit Features
Interactive UI
User input fields for session data
Real-time prediction
Clean dashboard layout
Run the application using:
streamlit run app.py

📂 Project Structure
Clickstream_Classification_Project
│
├── dataset.csv
├── notebook.ipynb
├── app.py
├── clickstream_model.pkl
├── scaler.pkl
└── README.md

Applications
This type of classification model can be used in:
E-commerce recommendation systems
User behavior analysis
Website personalization
Marketing analytics
Customer journey analysis

Future Improvements
Possible enhancements include:
Using advanced models like XGBoost or LightGBM
Hyperparameter tuning
Feature importance visualization
Model performance dashboard
Real-time API deployment
If you found this project useful, consider giving it a star on GitHub.
