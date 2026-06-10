import csv
from collections import defaultdict
import matplotlib.pyplot as plt
import numpy as np

# Read the CSV file and find employees who sold the same product on the same day at different prices
sales_by_product_date = defaultdict(list)

import streamlit as st
import pandas as pd
import plotly.express as px  # Or your preferred plotting library

st.title("Excel Data Analyzer")

# This creates the 'Upload' button on the website for the client
uploaded_file = st.file_uploader("Upload your Excel file here", type=["xlsx"])

if uploaded_file is not None:
    # Read the file the client just uploaded
    df = pd.read_excel(uploaded_file)
    
    st.write("### Data Preview", df.head())

    # Create a graph (example: a bar chart)
    fig = px.bar(df, x=df.columns[0], y=df.columns[1], title="Client Data Analysis")
    
    # This sends the graph back to the client's browser in Surat
    st.plotly_chart(fig)
else:
    st.info("Waiting for you to upload an Excel file...")

def compute_discrepancies(csv_path, top_n=20):
    """Reads the CSV and returns a DataFrame of top N discrepancies."""
    sales_by_product_date = defaultdict(list)
    with open(csv_path, mode='r', encoding='utf-8') as file:
        reader = csv.reader(file)
        header = next(reader, None)
        for row in reader:
            try:
                product_id = row[5]
                date = row[1]
                employee_id = row[4]
                total_amount = float(row[7])
            except Exception:
                continue
            key = (product_id, date)
            sales_by_product_date[key].append({'employee': employee_id, 'price': total_amount})

    discrepancies = []
    for (product_id, date), sales in sales_by_product_date.items():
        prices = [sale['price'] for sale in sales]
        unique_prices = set(prices)
        if len(unique_prices) > 1:
            max_price = max(prices)
            min_price = min(prices)
            difference = max_price - min_price
            discrepancies.append({
                'product': product_id,
                'date': date,
                'difference': difference,
                'min_price': min_price,
                'max_price': max_price,
                'employee_count': len(sales)
            })

    top = sorted(discrepancies, key=lambda x: x['difference'], reverse=True)[:top_n]
    rows = []
    for item in top:
        rows.append({
            'product': item['product'],
            'date': item['date'],
            'product_date': f"{item['product']} - {item['date']}",
            'difference': item['difference'],
            'min_price': item['min_price'],
            'max_price': item['max_price'],
            'employee_count': item['employee_count']
        })
    return pd.DataFrame(rows)