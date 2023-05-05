# -*- coding: utf-8 -*-
"""final_project_code_part2

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1PUTKF6-w4f-v08PUbwuR31OBdlgLwPDV

## DATA 606 - Capstone Project : Heart Disease Prediction Using Machine Learning
- Name : Sushanthik Reddy Poreddy
- ID: TY99095
- Professor: Chaojie Wang
"""

import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV, StratifiedKFold, cross_validate, RandomizedSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, f1_score, classification_report, precision_recall_curve, confusion_matrix

# Loading the DataSet
heart_df = pd.read_csv("https://raw.githubusercontent.com/SushanthikPoreddy/sushanthik_data606/main/data/heart_statlog_cleveland_hungary_final.csv")
heart_df.head()

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(heart_df.drop('target', axis=1), 
                                                    heart_df['target'], 
                                                    test_size=0.2, 
                                                    random_state=42)
print("Training DataSet Size:", (X_train.shape,y_train.shape),"\n""Test DataSet Size:", (X_test.shape,y_test.shape))

#scale data
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

print('\033[1m***Training RandomForest Classification Model:***\033[1m')

# Define a parameter grid to search over
params = {
    "class_weight": ['balanced', 'balanced_subsample'],
    "criterion": ['gini', 'entropy'],
    "max_features": ['auto', 'sqrt', 'log2'],
    "bootstrap" : [True, False]
}

# Create a RandomForestClassifier object with default hyperparameters
model_RFC = RandomForestClassifier(random_state=1)

# Create a StratifiedKFold object for cross-validation
cv_RFC = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)

# Create a RandomizedSearchCV object to search over the parameter grid
model_RFC_random_search = RandomizedSearchCV(model_RFC, param_distributions=params, scoring='f1', cv=cv_RFC, n_jobs=-1, verbose=3)

# Fit the RandomizedSearchCV object to your training data
model_RFC_random_search.fit(X_train, y_train)

# Print the best parameters found by RandomizedSearchCV
print("\033[1mBest parameters found by RandomizedSearchCV for Random Forest Classifier:\033[1m", model_RFC_random_search.best_params_)
# Print the best F1 score found by RandomizedSearchCV
print("\033[1mBest F1 score found by RandomizedSearchCV for Random Forest Classifier:\033[1m", model_RFC_random_search.best_score_)

y_predicted_test = model_RFC_random_search.best_estimator_.predict(X_test)
print("\033[1mClassification report generated from the results of RandomForestClassifier:\033[1m")
print(classification_report(y_test, y_predicted_test))

# Fit the model on the training data
model_RFC_random_search.fit(X_train, y_train)

# Get the predictions on new data
y_pred = model_RFC_random_search.predict(X_test)

# !pip install streamlit

import streamlit as st

# Define the UI layout
st.set_page_config(page_title="Heart Disease Prediction", page_icon=":heartbeat:")
st.title("Heart Disease Prediction")
st.sidebar.header("User Input Features")

# Create sliders for the user input features
def heart_health_predection():
    age = st.sidebar.slider('Age', 18, 100, 50)
    sex = st.sidebar.selectbox('Sex', ['male', 'female'])
    chest_pain_type = st.sidebar.selectbox('Chest Pain Type', [0, 1, 2, 3])
    resting_bp_s = st.sidebar.slider('Resting Blood Pressure (mm Hg)', 80, 200, 120)
    cholesterol = st.sidebar.slider('Serum Cholesterol (mg/dl)', 100, 600, 200)
    fasting_blood_sugar = st.sidebar.selectbox('Fasting Blood Sugar > 120 mg/dl', [0, 1])
    resting_ecg = st.sidebar.selectbox('Resting Electrocardiographic Results', [0, 1, 2])
    max_heart_rate = st.sidebar.slider('Maximum Heart Rate Achieved', 60, 200, 150)
    exercise_angina = st.sidebar.selectbox('Exercise Induced Angina', [0, 1])
    oldpeak = st.sidebar.slider('ST Depression Induced by Exercise Relative to Rest', 0.0, 6.0, 1.0)
    ST_slope = st.sidebar.selectbox('Slope of the Peak Exercise ST Segment', [0, 1, 2])
    sex = 1 if sex == 'male' else 0  # convert sex to binary
    data = {'age': age,
            'sex': sex,
            'chest pain type': chest_pain_type,
            'resting bp s': resting_bp_s,
            'cholesterol': cholesterol,
            'fasting blood sugar': fasting_blood_sugar,
            'resting ecg': resting_ecg,
            'max heart rate': max_heart_rate,
            'exercise angina': exercise_angina,
            'oldpeak': oldpeak,
            'ST slope': ST_slope}
    feature_set = pd.DataFrame(data, index=[0])
    return feature_set

# Create a dataframe from user input
heart_data = heart_health_predection()

# Scale the user input features
scaled_data = scaler.transform(heart_data)

# Get the prediction
prediction_result = model_RFC_random_search.predict(scaled_data)
prediction_proba = model_RFC_random_search.predict_proba(scaled_data)

# Print the prediction result
st.subheader('Prediction of Heart Health Status')
if prediction_result[0] == 0:
    st.write('Heart Disease is NOT present')
else:
    st.write('Heart Disease is present')

# Print the prediction probability
st.subheader('Prediction Probability')
st.write