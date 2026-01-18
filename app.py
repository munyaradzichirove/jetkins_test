from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!!"


@app.route("/webhook", methods=["POST"])
def webhook():
    if request.is_json:
        data = request.get_json()
    else:
        data = {"raw": request.data.decode("utf-8")}
    print("Webhook triggered!", data)

    # Call bash script to update app
    subprocess.Popen(["/home/munyaradzi/Downloads/flask_webhook/update_app.sh"])

    return jsonify({"status": "ok", "message": "Webhook triggered and update started!"})

if __name__ == "__main__": app.run(debug=True)