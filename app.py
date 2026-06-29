import json
import os
from flask import Flask, render_template, request
from database import create_table, insert_failure, get_failures, search_failures
from llm_helper import analyze_with_ai

app = Flask(__name__)

create_table()

LOG_FILE = "logs/failures.json"

os.makedirs("logs", exist_ok=True)

if not os.path.exists(LOG_FILE):
    with open(LOG_FILE, "w") as f:
        json.dump([], f, indent=4)


def load_failures():
    try:
        with open(LOG_FILE, "r") as f:
            return json.load(f)
    except:
        return []


def save_failures(data):
    with open(LOG_FILE, "w") as f:
        json.dump(data, f, indent=4)


@app.route("/")
def home():
    search = request.args.get("search", "").strip()

    if search:
        failures = search_failures(search)
    else:
        failures = get_failures()

    for failure in failures:
        failure["ai"] = analyze_with_ai(failure["error"])

    return render_template(
        "index.html",
        failures=failures,
        search=search
    )
@app.route("/debug")
def debug():
    from database import get_failures
    return {"count": len(get_failures()), "data": get_failures()}

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.get_json()

    if not data:
        return {"error": "No JSON"}, 400

    if "workflow_run" not in data:
        return {"message": "Ignored"}, 200

    workflow = data["workflow_run"]

    # ✅ IMPORTANT FIX: unique ID
    run_id = workflow.get("id")

    repo = data["repository"]["name"]
    workflow_name = workflow.get("name", "unknown")

    status = workflow.get("conclusion") or "unknown"
    time = workflow.get("updated_at", "")

    # ✅ Better error handling
    if status == "success":
        error = "Build Successful"
    elif status == "failure":
        error = "Build Failed (Check logs in GitHub Actions)"
    elif status == "cancelled":
        error = "Build Cancelled"
    else:
        error = f"Unknown status: {status}"

    # ✅ OPTIONAL: prevent duplicates (IMPORTANT)
    # You must implement this in DB layer
    # if not exists_run_id(run_id):

    insert_failure(
        repo,
        workflow_name,
        status,
        time,
        error,
        run_id   # ✅ add this in DB function too
    )

    print(f"Stored workflow run: {run_id}")

    return {"status": "success"}, 200


if __name__ == "__main__":
    app.run(debug=True)