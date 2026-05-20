# Step 2: Import Necessary Libraries
import streamlit as st
import numpy as np
import pandas as pd

# Step 3: Generate Random Sales Data
sales_data = np.random.rand(100) * 1000

# Step 4: Create a DataFrame
products = ['Product A', 'Product B', 'Product C', 'Product D', 'Product E']
sales = np.random.rand(5) * 1000
customers = np.random.randint(1, 100, size=5)

df = pd.DataFrame({
    'Product': products,
    'Sales': sales,
    'Customers': customers
})

# Step 5: Visualize Sales Data

# Display DataFrame using st.dataframe
st.markdown("### Product Sales and Customer Data")
st.dataframe(df)  # Interactive table with sorting and resizing

# Line Chart - Sales Over Time
st.markdown("### Sales Over Time")
st.line_chart(sales_data)

# Area Chart - Cumulative Sales
st.markdown("### Cumulative Sales")
st.area_chart(sales_data)

# Bar Chart - Sales by Product
st.markdown("### Sales by Product")
st.bar_chart(df[['Product', 'Sales']].set_index('Product'))

# Scatter Chart - Customer Engagement by Product
st.markdown("### Customer Engagement by Product")
st.scatter_chart(df[['Product', 'Customers']].set_index('Product'))


# Tabs Layout
tab1, tab2, tab3, tab4 = st.tabs(["Sales Data", 
                            "Customer Insights", 
                            "Market Trends",
                            "Market Performance",
                           ])
with tab1:
    st.write("Content for Sales Data")
    sales_data = {
        "Q1 2024": "$1.2M",
        "Q2 2024": "$1.5M",
        "Q3 2024": "$1.3M",
        "Q4 2024": "$1.6M"
    }
    for quarter, revenue in sales_data.items():
        st.write(f"{quarter}: {revenue}")
with tab2:
    st.write("Content for Customer Insights")
    customer_feedback = [
        "Great service!",
        "Very satisfied with the product quality.",
        "Quick delivery and excellent support."
    ]
    for feedback in customer_feedback:
        st.write(f"- {feedback}")
with tab3:
    st.write("Content for Market Trends")
    market_trends = {
        "Eco-friendly products": "Increasing demand",
        "Online shopping": "Continued growth",
        "Subscription services": "Rising popularity"
    }
    for trend, status in market_trends.items():
        st.write(f"{trend}: {status}")
with tab4:
    st.write("- To be confirmed")
    
with st.expander("More Information"):
    st.write("Additional details on data collection methods.")
    st.write("Data was collected through surveys and sales reports.")

# Dynamic Containers (placeholder)
placeholder = st.empty()

# Simulate loading data and updating the placeholder
for i in range(5):
    placeholder.write(f"Loading data... {i*20}% complete")
    time.sleep(1)

# Once loading is complete, display the final message
placeholder.write("Data loading complete. Displaying business insights.")

# Display dynamic business insights
business_insights = [
    "Revenue increased by 15% in Q1 2024.",
    "Customer satisfaction improved by 10%.",
    "Market trends show a growing demand for eco-friendly products."
]
for insight in business_insights:
    placeholder.write(insight)
    time.sleep(2)

st.subheader("Interactive Revenue Checker")
quarters = list(sales_data.keys())
selected_quarter = st.selectbox("Select a quarter:", quarters)

st.write(f"Revenue for {selected_quarter}: ${sales_data[selected_quarter]}M")

growth = st.slider("Adjust growth percentage:", 0, 50, 10)
base_revenue = sales_data[selected_quarter]
adjusted_revenue = base_revenue * (1 + growth / 100)

st.write(f"Adjusted Revenue for {selected_quarter}: ${adjusted_revenue:.2f}M")

# -------------------------------
# 7. Motivational Button
# -------------------------------
if st.button("Show Motivation"):
    st.success("Keep pushing for growth! 🚀")
