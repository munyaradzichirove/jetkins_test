from flask import Flask, request, jsonify
import subprocess

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!!333"

# Fix webhook route
@app.route("/webhook", methods=["POST", "GET"])
def webhook():
    # Optional: let GET just return a message (so testing in browser works)
    if request.method == "GET":
        return jsonify({"status": "ok", "message": "Send a POST to trigger the webhook"})

    # For POST requests
    if request.is_json:
        data = request.get_json()
    else:
        data = {"raw": request.data.decode("utf-8")}
    print("Webhook triggered!", data)

    # Call bash script asynchronously
    subprocess.Popen(["/home/munyaradzi/Downloads/flask_webhook/update_app.sh"])

    return jsonify({"status": "ok", "message": "Webhook triggered and update started!"})


if __name__ == "__main__":
    # Bind to 0.0.0.0 if you want it reachable from other machines
    app.run(debug=True, host="0.0.0.0", port=5000)
