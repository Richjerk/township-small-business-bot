from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/generate', methods=['POST'])
def generate():
    data = request.json
    model = data.get('model')
    prompt = data.get('prompt')
    response = f"This is a mock response for the model {model} with prompt: {prompt}"
    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=11434)
