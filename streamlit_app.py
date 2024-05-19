import streamlit as st
from geopy.geocoders import Nominatim
import requests
from PIL import Image
import ollama

# Function for LLM interaction using Ollama3
def query_ollama3(input_text):
    try:
        response = ollama.chat(model='llama3', messages=[{'role': 'user', 'content': input_text}])
        return response['message']['content']
    except Exception as e:
        st.error(f"Error querying Ollama3 API: {e}")
        return None

# Streamlit App
st.title("Township Small Business Chatbot")

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
        st.session_state["latitude"] = loc.latitude
        st.session_state["longitude"] = loc.longitude
    else:
        st.error("Location not found!")

# Products/Services Description
st.header("Products/Services")
product_services = st.text_area("Describe your products and services")

# Image Upload
st.header("Upload Business Images")
uploaded_files = st.file_uploader("Upload Images", accept_multiple_files=True, type=["jpg", "png", "jpeg"])
if uploaded_files:
    for uploaded_file in uploaded_files:
        img = Image.open(uploaded_file)
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
        "images": [uploaded_file.name for uploaded_file in uploaded_files]
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
        if response:
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

# Footer
st.write("---")
st.write("© 2024 Township Small Business Chatbot")



