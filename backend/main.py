import os
import requests
from dotenv import load_dotenv
from flask import Flask, jsonify, request
from flask_cors import CORS

load_dotenv()

app = Flask(__name__)
CORS(app)

def fetch_call_details(call_id):
    url = f"https://api.vapi.ai/call/{call_id}"
    headers = {
        "Authorization": f"Bearer {os.getenv('VAPI_API_KEY')}"
    }
    response = requests.get(url, headers=headers)
    return response.json()

# simple in-memory store of past call results (for demonstration)
call_records = []

@app.route("/call-details", methods=["GET"])
def get_call_details():
    call_id = request.args.get("call_id")
    if not call_id:
        return jsonify({"error": "Call ID is required"}), 400
    
    try:
        response = fetch_call_details(call_id)
        print(response)
        summary = response.get("summary")
        analysis = response.get("analysis")

        # store the result so it can be viewed later
        call_records.append({
            "call_id": call_id,
            "summary": summary,
            "analysis": analysis,
        })

        return jsonify({"analysis": analysis, "summary": summary}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
@app.route("/all-calls", methods=["GET"])
def list_all_calls():
    """Return all stored call records. This endpoint allows clients to fetch the history of every call detail that has been looked up so far."""
    return jsonify(call_records), 200


@app.route("/preview", methods=["GET"])
def preview_calls():
    """Simple HTML view of all stored calls for quick preview in a browser."""
    html = ["<html><head><title>Call Preview</title></head><body><h1>Stored Calls</h1><table border='1'><tr><th>Call ID</th><th>Qualified</th><th>Summary</th></tr>"]
    for c in call_records:
        qualified = c.get("analysis", {}).get("structuredData", {}).get("is_qualified")
        html.append(f"<tr><td>{c.get('call_id')}</td><td>{qualified}</td><td>{c.get('summary')}</td></tr>")
    html.append("</table></body></html>")
    return "".join(html)

if __name__ == "__main__":
    app.run(debug=True)