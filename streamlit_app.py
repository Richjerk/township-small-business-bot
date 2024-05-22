import streamlit as st
from geopy.geocoders import Nominatim
import requests
import os
import ollama
from PIL import Image
from auth import register_user, login_user
from ollama_api import query_ollama  # Import the function

# Your existing Streamlit code...

with open('style.css') as f:
    css = f.read()

# Mock function for LLM interaction using Ollama3
def query_ollama3(input_text):
    response = requests.post("https://api.ollama3.com/query", json={"input": input_text})
    return response.json()["response"]

# Streamlit App
st.title("Township Small Business Chatbot")

# Authentication and Registration (Placeholder)
def authenticate():
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        if username == "admin" and password == "password":
            st.session_state.authenticated = True
        else:
            st.error("Invalid credentials")

def register():
    new_username = st.text_input("New Username")
    new_password = st.text_input("New Password", type="password")
    if st.button("Register"):
        st.success("Registration successful! Please log in.")

if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

if not st.session_state.authenticated:
    st.sidebar.header("Login / Register")
    auth_option = st.sidebar.radio("Choose an option", ["Login", "Register"])
    if auth_option == "Login":
        authenticate()
    else:
        register()
    st.stop()

# Business Profile Input
st.header("Business Profile")
business_name = st.text_input("Business Name")
owner_name = st.text_input("Owner Name")
contact_info = st.text_input("Contact Information")

# GPS Location Input
st.header("GPS Location")
geolocator = Nominatim(user_agent="geoapiExercises")
location = st.text_input("Enter your location (Address, City, etc.)")
if st.button("Get Coordinates"):
    loc = geolocator.geocode(location)
    if loc:
        st.write(f"Coordinates: {loc.latitude}, {loc.longitude}")
        st.session_state.latitude = loc.latitude
        st.session_state.longitude = loc.longitude
    else:
        st.error("Location not found!")

# Products/Services Description
st.header("Products/Services")
product_services = st.text_area("Describe your products and services")

# Image Upload
st.header("Upload Business Images")
uploaded_files = st.file_uploader("Upload Images", accept_multiple_files=True, type=["jpg", "png", "jpeg"])
images = []
if uploaded_files:
    for uploaded_file in uploaded_files:
        img = Image.open(uploaded_file)
        images.append(img)
        st.image(img, caption=uploaded_file.name)

# Save Business Profile (Mock)
def save_business_profile():
    business_profile = {
        "business_name": business_name,
        "owner_name": owner_name,
        "contact_info": contact_info,
        "latitude": st.session_state.get("latitude"),
        "longitude": st.session_state.get("longitude"),
        "product_services": product_services,
        "images": [img.filename for img in images]
    }
    st.success("Business profile saved successfully!")
    return business_profile

if st.button("Save Profile"):
    business_profile = save_business_profile()

# Chat Page
st.header("Chat with Businesses")
user_query = st.text_input("Ask about local businesses")
if st.button("Send Query"):
    if user_query:
        response = query_ollama3(user_query)
        st.write("Response:", response)
    else:
        st.error("Please enter a query")

# Order Request (Uber-like)
st.header("Request an Order")
order_details = st.text_area("Enter order details (Product/Service, Quantity, etc.)")
if st.button("Request Order"):
    if order_details:
        st.success("Order requested successfully! A business will respond soon.")
        # In a real application, the order request would be sent to the businesses and tracked
    else:
        st.error("Please enter order details")

def main():
    st.title("Township Small Business Bot")

    # Example usage of the query_ollama function
    user_query = st.text_input("Ask about local businesses")
    if st.button("Send Query"):
        if user_query:
            response = query_ollama(user_query)  # Call the function with user input
            st.write("Response:", response)

if __name__ == "__main__":
    main()

# Footer
st.write("---")
st.write("© 2024 Township Small Business Chatbot")

