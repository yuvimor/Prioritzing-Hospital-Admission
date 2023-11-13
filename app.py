# streamlit_app.py
import streamlit as st
import joblib
import pandas as pd
from sklearn.preprocessing import LabelEncoder

# Load the trained model
model = joblib.load('model.joblib')

# Load the label encoder for 'Priority'
label_encoder = joblib.load('label_encoder.joblib')

# Streamlit app
st.title('Hospital Admission Priority Prediction App')

# Create a form for user input
st.sidebar.header('User Input')

# Include input fields for the relevant columns
user_input = {
    'AGE': st.sidebar.slider('Age', min_value=0, max_value=100, value=30),
    'TYPE OF ADMISSION-EMERGENCY/OPD': st.sidebar.radio('Type of Admission (1=OPD, 0=Emergency)', [1,0]),
    'CAD': st.sidebar.checkbox('Coronary Artery Disease (CAD)'),
    'PRIOR CMP': st.sidebar.checkbox('Cardiomyopathy (PRIOR CMP)'),
    'CKD': st.sidebar.checkbox('Chronic Kidney Disease (CKD)'),
    'RAISED CARDIAC ENZYMES': st.sidebar.checkbox('Raised Cardiac Enzymes'),
    'SEVERE ANAEMIA': st.sidebar.checkbox('Severe Anemia'),
    'STABLE ANGINA': st.sidebar.checkbox('Stable Angina'),
    'ACS': st.sidebar.checkbox('Acute Coronary Syndrome (ACS)'),
    'STEMI': st.sidebar.checkbox('ST Elevation Myocardial Infarction (STEMI)'),
    'HEART FAILURE': st.sidebar.checkbox('Heart Failure'),
    'HFREF': st.sidebar.checkbox('Heart Failure with Reduced Ejection Fraction (HFREF)'),
    'HFNEF': st.sidebar.checkbox('Heart Failure with Normal Ejection Fraction (HFNEF)'),
    'VALVULAR': st.sidebar.checkbox('Valvular Heart Disease'),
    'CHB': st.sidebar.checkbox('Complete Heart Block (CHB)'),
    'SSS': st.sidebar.checkbox('Sick Sinus Syndrome (SSS)'),
    'AKI': st.sidebar.checkbox('Acute Kidney Injury (AKI)'),
    'CVA INFRACT': st.sidebar.checkbox('Cerebrovascular Accident Infarction (CVA INFRACT)'),
    'CVA BLEED': st.sidebar.checkbox('Cerebrovascular Accident Bleed (CVA BLEED)'),
    'AF': st.sidebar.checkbox('Atrial Fibrillation (AF)'),
    'VT': st.sidebar.checkbox('Ventricular Tachycardia (VT)'),
    'CONGENITAL': st.sidebar.checkbox('Congenital Heart Disease'),
    'INFECTIVE ENDOCARDITIS': st.sidebar.checkbox('Infective Endocarditis'),
    'DVT': st.sidebar.checkbox('Deep Venous Thrombosis (DVT)'),
    'CARDIOGENIC SHOCK': st.sidebar.checkbox('Cardiogenic Shock'),
    'SHOCK': st.sidebar.checkbox('Shock'),
    'PULMONARY EMBOLISM': st.sidebar.checkbox('Pulmonary Embolism'),
    'CHEST INFECTION': st.sidebar.checkbox('Chest Infection'),
    'HB': st.sidebar.slider('Hemoglobin (HB)', min_value=0, max_value=20, value=10),
    'TLC': st.sidebar.slider('Total Leukocytes Count (TLC)', min_value=0, max_value=50, value=10),
    'PLATELETS': st.sidebar.slider('Platelets', min_value=0, max_value=500, value=200),
    'GLUCOSE': st.sidebar.slider('Glucose', min_value=0, max_value=300, value=100),
    'UREA': st.sidebar.slider('Urea', min_value=0, max_value=100, value=30),
    'CREATININE': st.sidebar.slider('Creatinine', min_value=0, max_value=5, value=1),
    'BNP': st.sidebar.slider('B-Type Natriuretic Peptide (BNP)', min_value=0, max_value=200, value=50),
    'EF': st.sidebar.slider('Ejection Fraction (EF)', min_value=0, max_value=100, value=60),
}

# Create a DataFrame with the user input
input_df = pd.DataFrame([user_input])

# Make predictions using the loaded model
prediction = model.predict(input_df)

# Map the numeric prediction back to the original labels
prediction_label = label_encoder.inverse_transform(prediction)[0]

# Display the prediction
st.subheader('Prediction:')
st.write(f'The predicted priority is: {prediction_label}')
