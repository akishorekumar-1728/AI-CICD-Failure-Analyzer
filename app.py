from flask import Flask, render_template, request

app = Flask(__name__)

builds = []

@app.route("/")
def home():
    return render_template("index.html", builds=builds)

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json

    print("Webhook Received")
    print(data)

    builds.append({
        "message": "Webhook received successfully"
    })

    return {"status": "success"}, 200

if __name__ == "__main__":
    app.run(debug=True)