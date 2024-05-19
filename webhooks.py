from flask import Flask, request, jsonify
from mailserver import *
app = Flask(__name__)


@app.route('/receive', methods=['POST'])
def webhook():
    data = request.json
    if data:
        # Process the data (for example, send an email)
        send_email(data)
        return jsonify({"message": "Data received and email sent!"}), 200
    else:
        return jsonify({"error": "No data received"}), 400


if __name__ == '__main__':
    app.run(port=8889)

