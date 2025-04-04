import streamlit as st
import requests

st.title("Reportify Frontend")

# Example API call (replace with your actual API endpoint)
api_url = "http://127.0.0.1:8000/"  # Your FastAPI backend URL

if st.button("Call API"):
    try:
        response = requests.get(api_url)
        response.raise_for_status()  # Raise an exception for bad status codes (4xx or 5xx)
        data = response.json()
        st.write("API Response:")
        st.write(data)
    except requests.exceptions.RequestException as e:
        st.error(f"Error calling API: {e}")

