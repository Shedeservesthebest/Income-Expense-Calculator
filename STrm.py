#!/usr/bin/env python
# coding: utf-8

# In[ ]:


'''import streamlit as st

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


import streamlit as st

# Streamlit app title
st.title("Income and Expenses Calculator")

# Initialize session states for income and expenses lists
if "income_items" not in st.session_state:
    st.session_state.income_items = []
    st.session_state.expense_items = []

# Function to add a new income source
def add_income():
    st.session_state.income_items.append({"name": "", "amount": 0.0})

# Function to add a new expense
def add_expense():
    st.session_state.expense_items.append({"name": "", "amount": 0.0})

# Input fields for income
st.subheader("Income Sources")
for i, income_item in enumerate(st.session_state.income_items):
    income_name = st.text_input(f"Income Source {i+1} Name", value=income_item["name"], key=f"income_name_{i}")
    income_amount = st.number_input(f"Income Source {i+1} Amount", min_value=0.0, format="%.2f", value=income_item["amount"], key=f"income_amount_{i}")
    st.session_state.income_items[i]["name"] = income_name
    st.session_state.income_items[i]["amount"] = income_amount

# Button to add a new income source
if st.button("Add New Income Source"):
    add_income()

# Input fields for expenses
st.subheader("Expenses")
for i, expense_item in enumerate(st.session_state.expense_items):
    expense_name = st.text_input(f"Expense {i+1} Name", value=expense_item["name"], key=f"expense_name_{i}")
    expense_amount = st.number_input(f"Expense {i+1} Amount", min_value=0.0, format="%.2f", value=expense_item["amount"], key=f"expense_amount_{i}")
    st.session_state.expense_items[i]["name"] = expense_name
    st.session_state.expense_items[i]["amount"] = expense_amount

# Button to add a new expense
if st.button("Add New Expense"):
    add_expense()

# Calculate total income and expenses
total_income = sum(item["amount"] for item in st.session_state.income_items)
total_expenses = sum(item["amount"] for item in st.session_state.expense_items)
balance = total_income - total_expenses

# Display the balance
if st.button("Calculate Balance"):
    if total_income == 0:
        st.write("Please enter valid income sources.")
    elif total_expenses > total_income:
        st.write(f"Warning: Your expenses exceed your income! You are in deficit by {abs(balance):.2f}.")
    else:
        st.write(f"Your remaining balance is: {balance:.2f}")'''



import streamlit as st
# Streamlit app title
st.title("Income and Expenses Calculator")

# Initialize session states for income and expenses lists
if "income_items" not in st.session_state:
    st.session_state.income_items = []
    st.session_state.expense_items = []

# Function to add a new income source
def add_income():
    st.session_state.income_items.append({"name": "", "amount": 0.0})

# Function to add a new expense
def add_expense():
    st.session_state.expense_items.append({"name": "", "amount": 0.0})

# Function to remove empty income or expense entries
def remove_empty_entries():
    # Remove income items with empty name or zero amount
    st.session_state.income_items = [item for item in st.session_state.income_items if item['name'] and item['amount'] > 0]

    # Remove expense items with empty name or zero amount
    st.session_state.expense_items = [item for item in st.session_state.expense_items if item['name'] and item['amount'] > 0]

# Input fields for income
st.subheader("Income Sources")
for i, income_item in enumerate(st.session_state.income_items):
    income_name = st.text_input(f"Income Source {i+1} Name", value=income_item["name"], key=f"income_name_{i}")
    income_amount = st.number_input(f"Income Source {i+1} Amount", min_value=0.0, format="%.2f", value=income_item["amount"], key=f"income_amount_{i}")
    st.session_state.income_items[i]["name"] = income_name
    st.session_state.income_items[i]["amount"] = income_amount

# Button to add a new income source
if st.button("Add New Income Source"):
    add_income()

# Input fields for expenses
st.subheader("Expenses")
for i, expense_item in enumerate(st.session_state.expense_items):
    expense_name = st.text_input(f"Expense {i+1} Name", value=expense_item["name"], key=f"expense_name_{i}")
    expense_amount = st.number_input(f"Expense {i+1} Amount", min_value=0.0, format="%.2f", value=expense_item["amount"], key=f"expense_amount_{i}")
    st.session_state.expense_items[i]["name"] = expense_name
    st.session_state.expense_items[i]["amount"] = expense_amount

# Button to add a new expense
if st.button("Add New Expense"):
    add_expense()

# Button to remove empty entries
if st.button("Remove Empty Entries"):
    remove_empty_entries()

# Calculate total income and expenses
total_income = sum(item["amount"] for item in st.session_state.income_items)
total_expenses = sum(item["amount"] for item in st.session_state.expense_items)
balance = total_income - total_expenses

# Display the balance
if st.button("Calculate Balance"):
    if total_income == 0:
        st.write("Please enter valid income sources.")
    elif total_expenses > total_income:
        st.write(f"Warning: Your expenses exceed your income! You are in deficit by {abs(balance):.2f}.")
    else:
        st.write(f"Your remaining balance is: {balance:.2f}")
