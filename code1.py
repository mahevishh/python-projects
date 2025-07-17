import streamlit as st
import pandas as pd 
import numpy as np 

st.title("My Streamlit App")
st.write("This is a simple app to demostreate the basic functionalities of Streamlit")

st.header("User input Features")

user_name = st.sidebar.text_input("what is your name?","Streamlit user")

age = st.sidebar.slider("select your age",0,100,25)

fav_color = st.sidebar.selectbox("What is your favorite color?",["Blue","Red","Green","Yellow","purple","Pink","White","others"])

st.header(f"Welcom, {user_name}")
st.write(f"you are {age} years old and your Favorite color is {fav_color}")

st.subheader("Here's some random data:")

# Create a sample DataFrame
data = pd.DataFrame(
    np.random.randn(10, 5),
    columns=('col %d' % i for i in range(5))
)

st.dataframe(data)

# --- Checkbox to show/hide content ---
if st.checkbox("Show raw data"):
    st.subheader("Raw Data")
    st.write(data)

# --- Button to trigger an action ---
if st.button("Say hello"):
    st.write("Hello there!")
else:
    st.write("Goodbye")