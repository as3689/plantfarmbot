
from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # 모든 엔드포인트에 대해 CORS 활성화

@app.route('/api/chatbot', methods=['POST'])
def chatbot():
    user_input = request.json.get('message')
    response = f"You said: {user_input}"
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)
