from flask import Flask, jsonify, request
from flask_cors import CORS
import requests
import os
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)
CORS(app)

OTX_API_KEY = os.getenv("OTX_API_KEY")

@app.route('/')
def get_pulses():
    try:
        url = "https://otx.alienvault.com/api/v1/pulses/subscribed"
        headers = {"X-OTX-API-KEY": OTX_API_KEY}
        response = requests.get(url, headers=headers)
        pulses = response.json().get("results", [])
        normalized = normalize_data(pulses)

        # 🔍 Apply optional filters from query params
        indicator_type = request.args.get("indicator_type")
        severity = request.args.get("severity")
        source = request.args.get("source")
        tag = request.args.get("tag")

        if indicator_type:
            normalized = [n for n in normalized if n["indicator_type"].lower() == indicator_type.lower()]
        if severity:
            normalized = [n for n in normalized if n["severity"].lower() == severity.lower()]
        if source:
            normalized = [n for n in normalized if n["source"].lower() == source.lower()]
        if tag:
            normalized = [n for n in normalized if tag.lower() in n["tags"].lower()]

        return jsonify(normalized)

    except Exception as e:
        return jsonify({"error": str(e)}), 500

def normalize_data(pulses):
    normalized = []
    for pulse in pulses:
        pulse_id = pulse.get("id")
        name = pulse.get("name", "Unnamed Pulse")
        description = pulse.get("description", "")
        source = "OTX"
        severity = pulse.get("TLP", "amber")
        created = pulse.get("created", "unknown")
        tags = ", ".join(pulse.get("tags", []))  # Join tags list into a single string

        indicators = pulse.get("indicators", [])
        for ioc in indicators:
            normalized.append({
                "pulse_id": pulse_id,
                "pulse_name": name,
                "description": description,
                "indicator_type": ioc.get("type", "unknown"),
                "indicator_value": ioc.get("indicator", "unknown"),
                "created": created,
                "severity": severity,
                "source": source,
                "tags": tags
            })
    return normalized

if __name__ == "__main__":
    app.run(debug=True, port=5000)
