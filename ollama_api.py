from fastapi import FastAPI

app = FastAPI()

@app.post("/ollama")
def generate_response(prompt: str):
    # Replace with your actual Llama 2 model invocation
    model_response = ollama.generate(prompt, model="llama3", temperature=0.8)
    return {"response": model_response}
