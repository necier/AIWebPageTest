from flask import Flask, request, jsonify
from flask_cors import CORS


app = Flask(__name__)

def get_bot_reply(message):
    return f"You said: {message}"

@app.route('/chatbot', methods=['POST'])
def chatbot():
    data = request.get_json()
    message = data['message']
    reply = get_bot_reply(message)
    return jsonify(reply=reply)

if __name__ == '__main__':
    CORS(app, resources={r"*": {"origins": "*"}})
    app.run(debug=True)
