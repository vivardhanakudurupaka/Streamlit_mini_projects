import streamlit as st

st.title("PROGRAMMING LANGUAGE")
st.header("please select your programming language")
programming = st.selectbox("your language ",["JAVA" , "PYTHON" , "C++" , "C" ])
st.write(f"{programming} is the language that you have choosed")
st.success("you have successfully choosed your programming language")