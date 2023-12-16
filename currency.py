import streamlit as st
from forex_python.converter import CurrencyRates

def convert_currency(amount, source_currency, target_currency):
    c = CurrencyRates()
    conversion_rate = c.get_rate(source_currency, target_currency)
    converted_amount = amount * conversion_rate
    return converted_amount

# Title of the app
st.title("Currency Converter")

# Input options
amount = st.number_input("Enter the amount to convert", min_value=0.01, step=0.01)
source_currency = st.selectbox("Select the source currency", ["USD", "EUR", "GBP", "JPY", "AUD"])
target_currency = st.selectbox("Select the target currency", ["USD", "EUR", "GBP", "JPY", "AUD"])

# Convert currency when the user clicks the button
if st.button("Convert"):
    converted_amount = convert_currency(amount, source_currency, target_currency)
    st.success(f"{amount} {source_currency} is equal to {converted_amount:.2f} {target_currency}")

# Add a footer
st.text("Built by Shwetha ")
