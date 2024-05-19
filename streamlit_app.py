import streamlit as st
<<<<<<< HEAD
from geopy.geocoders import Nominatim
import requests
import os
from PIL import Image

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

# Footer
st.write("---")
st.write("© 2024 Township Small Business Chatbot")


=======

# In-memory storage for businesses
businesses = []

def add_business(name, type, address):
    businesses.append({"name": name, "type": type, "address": address})

def view_businesses():
    return businesses

def update_business(name, new_type, new_address):
    for business in businesses:
        if business["name"] == name:
            business["type"] = new_type
            business["address"] = new_address
            return True
    return False

def delete_business(name):
    for business in businesses:
        if business["name"] == name:
            businesses.remove(business)
            return True
    return False

def main():
    st.title("Township Small Business Chatbot")

    menu = ["Add Business", "View Businesses", "Update Business", "Delete Business"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Add Business":
        st.subheader("Add a New Business")
        name = st.text_input("Business Name")
        type = st.text_input("Business Type")
        address = st.text_input("Business Address")
        if st.button("Add Business"):
            add_business(name, type, address)
            st.success(f"Added {name}")

    elif choice == "View Businesses":
        st.subheader("View All Businesses")
        businesses_list = view_businesses()
        for business in businesses_list:
            st.write(business)

    elif choice == "Update Business":
        st.subheader("Update Business")
        name = st.text_input("Business Name to Update")
        new_type = st.text_input("New Business Type")
        new_address = st.text_input("New Business Address")
        if st.button("Update Business"):
            if update_business(name, new_type, new_address):
                st.success(f"Updated {name}")
            else:
                st.error(f"Business {name} not found")

    elif choice == "Delete Business":
        st.subheader("Delete Business")
        name = st.text_input("Business Name to Delete")
        if st.button("Delete Business"):
            if delete_business(name):
                st.success(f"Deleted {name}")
            else:
                st.error(f"Business {name} not found")

if __name__ == '__main__':
    main()


>>>>>>> 71b545d9b762aee383acc12e48fa8c8847d95b0b
