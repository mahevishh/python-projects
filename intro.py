import streamlit as st

st.title("my first streamlit app created by Shora Mahevish")

st.write("WElcome! This app calculates the squre of a number")

st.header("select a Number")
number= st.slider("pick a number",0,100,25) #min, max, default

#calculate and display the result
st.subheader("Result")
squared_number = number * number
st.write(f"The square of **{number}** is **{squared_number}**.")

