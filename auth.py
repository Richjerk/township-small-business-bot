# auth.py
import hashlib
from db import get_users_collection

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def register_user(username, email, password):
    users_collection = get_users_collection()
    if users_collection.find_one({"email": email}):
        return "User already exists"
    
    hashed_password = hash_password(password)
    user = {
        "username": username,
        "email": email,
        "password": hashed_password
    }
    users_collection.insert_one(user)
    return "User registered successfully"

def login_user(email, password):
    users_collection = get_users_collection()
    user = users_collection.find_one({"email": email})
    
    if not user:
        return "Invalid credentials"
    
    hashed_password = hash_password(password)
    if user['password'] != hashed_password:
        return "Invalid credentials"
    
    return "Login successful"

