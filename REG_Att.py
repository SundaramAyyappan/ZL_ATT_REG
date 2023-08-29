# -*- coding: utf-8 -*-
"""
Created on Tue Aug 29 10:18:51 2023

@author: 103925suay
"""
import pickle
import streamlit as st 
import numpy as np
import pandas as pd 

# For creating encoded label dict
def label_encoder_maker(excel):
    return_dict = {}
    csvfile = pd.read_excel(excel, sheet_name=None)
    for sheet in csvfile.keys():
        jc_df = csvfile[sheet]
        jc_dict = jc_df.set_index('Row Labels').to_dict()['Code']
        return_dict[sheet] = jc_dict
        
    return return_dict

pickle_in = open("modelLR.pickle","rb")
regressor=pickle.load(pickle_in)

def welcome():
    return "Welcome Zalaris Recuriters"

def Candidate_prediction(Gender, Employee_Group, Country, Business_Unit,Job_Classification, Supervisor,Divison, Age):
    test_data = pd.DataFrame([[Gender, Employee_Group, Country, Business_Unit,Job_Classification, Supervisor,Divison,Age]],
                         columns=['Gender','Employee_Group','Country','Business_Unit','Divison','Job_Classification','Supervisor','Age'])
    predicted_duration = regressor.predict(test_data)
    
    return f"Predicted stay duration: {predicted_duration[0]:.2f} years"

encoder_excel_path = "LE_code_reg.xlsx"
feature_dict = label_encoder_maker(encoder_excel_path)

# feature_dict
job_class_dict = feature_dict['Max of Job Classification']
jobclass_tuple = tuple([key for key in job_class_dict.keys()])

Supervisor_dict = feature_dict['Max of Supervisor ']
supervisor_tuple = tuple([key for key in Supervisor_dict.keys()])

Divison_dict = feature_dict['Max of Divison']
Divison_tuple = tuple([key for key in Divison_dict.keys()])

Employee_group_dict = feature_dict['Max of Employee Group2']
Employee_group_tuple = tuple([key for key in Employee_group_dict.keys()])

Country_dict = feature_dict['Max of Country2']
Country_tuple = tuple([key for key in Country_dict.keys()])

Business_unit_dict = feature_dict['Max of Business Unit2']
Business_unit_tuple = tuple([key for key in Business_unit_dict.keys()])

Gender_dict = feature_dict['Gender']
Gender_tuple = tuple([key for key in Gender_dict.keys()])



def main():
    
    st.title('Zalaris Web App')
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Candiate Prediction Zalaris </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    
    Gender_selection = st.sidebar.selectbox('Gender',Gender_tuple)
    Gender = Gender_dict[Gender_selection]
    
    Employee_Group_selection = st.sidebar.selectbox('Employee_Group',Employee_group_tuple)
    Employee_Group = Employee_group_dict[Employee_Group_selection]
    
    
    Country_selection = st.sidebar.selectbox('Country',Country_tuple)
    Country = Country_dict[Country_selection]
    
    
    
    
    
    Age= st.sidebar.number_input('Insert  Age ')
    
    Business_Unit_selection = st.sidebar.selectbox('Business_unit',Business_unit_tuple)
    Business_Unit = Business_unit_dict[Business_Unit_selection]
    
    Divison_selection = st.sidebar.selectbox('Divison',Divison_tuple)
    Divison = Divison_dict[Divison_selection]
    
    
    Job_Classification_selection = st.sidebar.selectbox('Job_Classification',jobclass_tuple)
    Job_Classification = job_class_dict[Job_Classification_selection]
    
    
    Supervisor_selection = st.sidebar.selectbox('Supervisor',supervisor_tuple)
    Supervisor = Supervisor_dict[Supervisor_selection]
    
    
    #code for prediction (the result of prediction will return in this empty string)
    Candidate = ''
    
    #creating button for prediction
    if st.button('Candidate Result'):
        Candidate = Candidate_prediction(Gender, Employee_Group, Country, Business_Unit, Divison,Job_Classification, Supervisor, Age)
    
    
    st.success(Candidate)
    
    
    
if __name__ == '__main__':
    main()
