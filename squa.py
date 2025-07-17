#Streamlit is library used to built fronted applications
import streamlit as st 
st.title("First Streamlit app created by Sahithi")
st.write("Welcome! This app calculates the square of a number.")
#Create an interactive slider
st.header("Select a Number")
number = st.slider("Pick a number",0,200,25)#min max default 
#5 Calculate and display Result 
st.subheader("Result")
squared_number=number * number 
st.write(f"The square of **{number}** is **{squared_number}**.")