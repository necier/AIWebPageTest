from flask import Flask, request, jsonify
from flask_cors import CORS

import turbo_server

app = Flask(__name__)

def get_bot_reply(message):
    return str(turbo_server.returnReply(message))

def reset_data():
    turbo_server.reset_messages()

@app.route('/chatbot', methods=['POST'])
def chatbot():
    data = request.get_json()
    message = data['message']
    reply = get_bot_reply(message)
    return jsonify(reply=reply)

@app.route('/reset', methods=['POST'])
def reset():    
    # 在此处重置您的后端数据
    reset_data()
    return jsonify(status='success')
if __name__ == '__main__':
    CORS(app, resources={r"*": {"origins": "*"}})
    app.run(debug=True)
