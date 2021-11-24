import streamlit as st
import pandas as pd
import numpy as np
import pickle

# st.title('Predict Insurance cost')

st.markdown("<h1 style='text-align: center; color: Red;'>Predict Insurance Cost</h1>", unsafe_allow_html=True)
pipe_cat = pickle.load(open('pipe_cat.pkl','rb'))
pipe_xgb = pickle.load(open('pipe_xgb.pkl','rb'))
pipe_rf = pickle.load(open('pipe_rf.pkl','rb'))

col1,col2 = st.columns(2)
with col1:
    f_name = st.text_input('Enter First Name ') 
with col2:
    l_name = st.text_input('Enter Last Name')

age = st.slider('Select Age',min_value = 18 , max_value=70 , step=1)
col3,col4,col5 = st.columns(3)
with col3:
    sex = st.radio("Select Gender: ", ('male', 'female'))

with col4:
    smoker = st.radio("Smoker (Yes/No): ", ('yes', 'no'))

with col5:
    children = st.number_input('Number of Childern',min_value = 0 , max_value = 5 , step=1)

bmi = st.number_input('Enter BMI',min_value = 14.00 , max_value = 55.00,step = 0.1)

region = st.selectbox('Select Region',options=['southwest', 'southeast', 'northwest', 'northeast'])

if st.button('Predict Insurance cost'):
    error='N'
    if not f_name:
        st.warning('Please enter required First name')
        error='Y'
    if error=='N' and not l_name:
        st.warning('Please enter required Last name')
        error='Y'
    if error=='N':
        input_df = pd.DataFrame({  'age':[age] , 'sex':[sex] , 'bmi' : [bmi] , 'children' : [children] , 'smoker' : [smoker] , 'region' : [region]

        })
        y_pred_cat = pipe_cat.predict(input_df)
        y_pred_xgb = pipe_xgb.predict(input_df)
        y_pred_rf = pipe_rf.predict(input_df)

        result = (6*y_pred_cat + 2.5*y_pred_xgb+ 1.5*y_pred_rf)/10
        st.header('Predicted insurance cost for '+f_name+' '+l_name + ' is - %.2f'%(float(result)) + ' $')
