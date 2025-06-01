from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

BOT_TOKEN = "8041727281:AAGzXNoyYNG3tp7PVV-NQfLyN6tsolW8ShM"
MESSAGE = "🤖 Your verification was successful!"

@app.route('/send', methods=['POST'])
def send_message():
    data = request.json
    chat_id = data.get('chat_id')
    if not chat_id:
        return jsonify({"error": "chat_id missing"}), 400

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": MESSAGE
    }
    r = requests.post(url, json=payload)
    return jsonify(r.json())

if __name__ == '__main__':
    app.run(debug=True)