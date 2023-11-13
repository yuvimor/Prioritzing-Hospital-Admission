# PrioritzingHospital-Admission

This repository contains code and resources for prioritizing hospital admission according to emergency.

## Dataset Details

- **Data Source**: Hero DMC Heart Institute, Unit of Dayanand Medical College and Hospital
- **Study Period**: 1 April 2017 to 31 March 2019
- **Total Admissions**: 14,845
- **Unique Patients**: 12,238
- **Patients with Multiple Admissions**: 1,921

### Data Columns

- **Demographics**: Age, Sex, Locality (Rural or Urban)
- **Admission Details**: Date of Admission, Date of Discharge, Type of Admission (Emergency or Outpatient)
- **Patient History**: Smoking, Alcohol, Diabetes Mellitus (DM), Hypertension (HTN), Prior Coronary Artery Disease (CAD), Prior Cardiomyopathy (CMP), Chronic Kidney Disease (CKD)
- **Lab Parameters**: Hemoglobin (HB), Total Lymphocyte Count (TLC), Platelets, Glucose, Urea, Creatinine, Brain Natriuretic Peptide (BNP), Raised Cardiac Enzymes (RCE), Ejection Fraction (EF)
- **Comorbidities and Features**: Heart Failure, STEMI, Pulmonary Embolism, and 25 other features

## Notebooks

**Module 1**: 
   - Exploratory Data Analysis (EDA)
   - Data Preprocessing
   - Train-Test Split

**Module 2**:
   - Includes Module 1
   - Decision Tree Classifier Training and Model Saving (joblib)

## Streamlit App Deployment

The predictive model developed using this dataset has been deployed as a Streamlit app. To interact with the app, visit https://prioritzing-hospital-admission.streamlit.app/

Feel free to explore the provided Jupyter notebooks for a detailed walkthrough of the data analysis and model development process.
