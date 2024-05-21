from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/generate', methods=['POST'])
def generate_response():
    data = request.json
    model = data.get('model')
    prompt = data.get('prompt')
    if model and prompt:
        # Mock response for demonstration
        response = {
            "model": model,
            "prompt": prompt,
            "response": "The sky is blue due to the scattering of sunlight by the atmosphere."
        }
        return jsonify(response), 200
    else:
        return jsonify({"error": "Invalid input"}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=11434)
