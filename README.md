# CTI Dashboard
## Setup
1. Clone the repo: `git clone https://github.com/yourname/cti-dashboard.git`
2. Backend: 
   - Install dependencies: `pip install -r requirements.txt`
   - Run: `FLASK_APP=app.py flask run`
3. Frontend:
   - Install dependencies: `npm install`
   - Run: `npm start`

## Execution Instructions
```bash
cd backend
python -m venv venv
.\venv\Scripts\activate # Windows: venv\Scripts\activate  
pip install -r requirements.txt
flask run
```

## Data Sources
- **OTX**: AlienVault Open Threat Exchange
- **AbuseIPDB** (optional)

## Implementation Notes
- Normalized data schema: { id, name, description, indicators[], severity, source }
- Filtering by indicator type and severity