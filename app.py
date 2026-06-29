import json
from flask import Flask, render_template, request
from ai_helper import analyze_error

app = Flask(__name__)

# Store webhook events in memory
failures = []

@app.route("/")
def home():
    return render_template("index.html", failures=failures)


@app.route("/webhook", methods=["POST"])
def webhook():

    data = request.json

    print("========== WEBHOOK RECEIVED ==========")
    print(data)

    workflow = data.get("workflow_run", {})

    repo = data.get("repository", {}).get("name", "Unknown Repository")
    workflow_name = workflow.get("name", "Unknown Workflow")
    status = workflow.get("conclusion", "Unknown")
    time = workflow.get("updated_at", "Unknown Time")

    error = "No error log available"

    if status != "success":
        error = "GitHub Action failed."

    failure = {
        "repo": repo,
        "workflow": workflow_name,
        "status": status,
        "time": time,
        "error": error,
        "ai": analyze_error(error)
    }

    failures.insert(0, failure)

    return {"message": "Webhook received"}, 200


if __name__ == "__main__":
    app.run(debug=True)