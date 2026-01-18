from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json
    print("Webhook triggered!", data)
    return jsonify({"status": "ok", "message": "Webhook triggered!"})

if __name__ == "__main__":
    app.run(debug=True)
