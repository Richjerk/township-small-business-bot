import requests

def query_ollama(prompt):
    url = "http://127.0.0.1:11434/api/generate"
    payload = {
        "model": "llama3",
        "prompt": prompt
    }
    headers = {
        "Content-Type": "application/json"
    }

    response = requests.post(url, json=payload, headers=headers)
    
    if response.status_code == 200:
        return response.json().get("response", "")
    else:
        return f"Error: {response.status_code}, {response.text}"
