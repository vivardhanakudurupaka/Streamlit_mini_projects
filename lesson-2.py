import streamlit as st
from datetime import date

Today = date.today()
st.title("AGE CALCULATION")
st.header("Calculate your age with this app")

user_date = st.date_input("Enter your date-of-birth" ,value = date(2000,1,1))
age = Today.year - user_date.year

if (user_date.year,user_date.month) < (Today.year,Today.month) :
    age-=1
    st.write(f"your current age is {age}")
