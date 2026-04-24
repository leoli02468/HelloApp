import streamlit as st

st.title("Retail Business Dashboard")
st.header("Manager Input Section")

st.write("Please enter the monthly sales target and the region.")
         

monthly_sales = st.number_input("Enter Monthly Sales Target (in USD): ",
                     min_value=0,
                     max_value=50000,
                     value=50000)
st.write(f"The sales target entered: ${monthly_sales}")
                      
region = st.selectbox("Select Region:",
                     ["North", "South", "East", "West"])
st.write(f"The selected region: {region}")

if st.button("Submit"):
    st.success("Dashboard updated successfully!")


