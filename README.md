# CTI Dashboard
## Setup
1. Clone the repo: `git clone https://github.com/yourname/cti-dashboard.git`
2. Backend: 
   - Install dependencies: `pip install -r requirements.txt`
   - Run: `FLASK_APP=app.py flask run`
3. Frontend:
   - Install dependencies: `npm install`
   - Run: `npm start`

## Data Sources
- **OTX**: AlienVault Open Threat Exchange
- **AbuseIPDB** (optional)

## Implementation Notes
- Normalized data schema: { id, name, description, indicators[], severity, source }
- Filtering by indicator type and severity