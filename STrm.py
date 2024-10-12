#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import streamlit as st

# Streamlit app title
st.title("Income and Expenses Calculator")

# Input fields for customer income and expenses
income = st.number_input("Enter your total income:", min_value=0.0, format="%.2f")
expenses = st.number_input("Enter your total expenses:", min_value=0.0, format="%.2f")

# Calculate remaining balance
balance = income - expenses

# Display the balance
if st.button("Calculate"):
    if income == 0:
        st.write("Please enter a valid income.")
    elif expenses > income:
        st.write(f"Warning: Your expenses exceed your income! You are in deficit by {abs(balance):.2f}.")
    else:
        st.write(f"Your remaining balance is: {balance:.2f}")

