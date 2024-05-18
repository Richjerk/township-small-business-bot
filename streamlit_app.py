import streamlit as st

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
