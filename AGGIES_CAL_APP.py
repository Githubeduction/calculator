#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 26 11:43:03 2023

@author: aggie
"""

import streamlit as st
import base64
import PIL

st.set_page_config(
    page_title = "Calculator App",
    layout = "centered",
    initial_sidebar_state = "auto"
    )

st.title("AGGIE'S simple Calculator App using Streamlit")

col1, col2 = st.columns([1, 1])
with col1: 
    st.image("pexels-yaroslav-shuraev-6283223.jpg") 
with col2: 
    st.write("""To get the exact figures of what you are calculating without complexities you need a simple calculator like this one, you can add, multiply , subtract and divide numbers so that your figures can never be wrong""")

# creates a horizontal line
st.write("---")
 
# input 1
num_1 = st.number_input(label="Enter first number")
 
# input 2
num_2 = st.number_input(label="Enter second number")
 
st.write("Operation")
 
operation = st.radio("Select an operation to perform:",
                    ("Add", "Subtract", "Multiply", "Divide"))
 
ans = 0
 
def calculate():
    if operation == "Add":
        ans = num_1 + num_2
    elif operation == "Subtract":
        ans = num_1 - num_2
    elif operation == "Multiply":
        ans = num_1 * num_2
    elif operation=="Divide" and num_2!=0:
        ans = num_1 / num_2
    else:
        st.warning("Division by 0 error. Please enter a non-zero number.")
        ans = "Not defined"
 
    st.success(f"Answer = {ans}")
 
if st.button("Calculate result"):
    calculate()    
 
    
    
