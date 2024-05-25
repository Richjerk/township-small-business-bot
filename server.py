from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/modelfiles/create', methods=['POST'])
def create_model():
    # Extract data from request
    data = request.get_json()

    # TODO: Add your chatbot logic here

    # Return a response
    return jsonify({"message": "Model created successfully"}), 200

if __name__ == '__main__':
    app.run(host='localhost', port=11434)
