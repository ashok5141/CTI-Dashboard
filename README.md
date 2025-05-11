# Cyber Threat Intelligence Dashboard - OTX Pulses

Dashboard Overview The **Cyber Threat Intelligence Dashboard** provides an intuitive interface for visualizing cyber threat intelligence data retrieved from the AlienVault OTX API. The dashboard allows users to filter and analyze different threat indicators, including CVE, file hashes (MD5, SHA1, SHA256), URLs, and domains. ### Key Features:
 - **Filter Indicators**: Easily filter the data by indicator type (e.g., Filehash SHA256, URL, CVE), severity (e.g., amber), and source (e.g., OTX). 
 - **Indicator Type Distribution**: A bar chart displaying the distribution of indicator types across different threats. 
 - **Severity Breakdown**: A pie chart visualizing the breakdown of threat severities, enabling quick identification of the threat landscape. 
 - **Summary**: Displays the total number of indicators and the number of unique pulses, offering quick insights into the data. This dashboard enables security professionals to quickly assess the latest cyber threats and filter relevant information, improving incident response and decision-making. 
</br></br>


![CTI Dashboard](/Images/CTI_Dashboard.png)



## Setup
- Clone the repo: `git clone https://github.com/ashok5141/CTI-Dashboard`

## OTX API key
- Register or login account https://otx.alienvault.com/api.
- Replace API key with your own key in the `\backend\.env` file.

## Execution Instructions for flask app/flask server
- First terminal
```bash
cd backend
python -m venv venv
.\venv\Scripts\activate # Windows: venv\Scripts\activate  
pip install -r requirements.txt
flask run  # It will run the app.py, http://127.0.0.1:5000/ 
Filter Indicators
 #http://127.0.0.1:5000/?indicator_type=domain(choose the parameter of your choice)
 #http://127.0.0.1:5000/?severity=amber
 #http://127.0.0.1:5000/?source=OTX
```

## Execution Instructions for streamlit for visualization
- Second terminal
```bash
cd backend
python -m venv venv
.\venv\Scripts\activate # Windows: venv\Scripts\activate  
streamlit run dashboard.py  #Automatically opens  this path  http://192.168.0.13:8501
```
</br>

### CTI Rawdata

 ![CTI Dashboard](/Images/CTI_RawData.png)

## Implementation Notes
- Normalized data schema: { id, name, description, indicators[], severity, source }
- Filtering by indicator type and severity

## Data Sources
- **OTX**: AlienVault Open Threat Exchange