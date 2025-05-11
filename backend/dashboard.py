import streamlit as st
import pandas as pd
import requests
import json
import plotly.express as px  # Add this at the top of your script

# Set the page title and layout
st.set_page_config(page_title="CTI Dashboard", layout="wide")
st.title("Cyber Threat Intelligence Dashboard - OTX Pulses")

# Fetch data from Flask API endpoint
api_url = "http://127.0.0.1:5000/"  # Correct Flask API URL (should match your Flask server's port)
response = requests.get(api_url)

# Check if the response is in JSON format
if response.status_code == 200:
    try:
        # Attempt to parse JSON
        data = response.json()
        
        # If successful, convert to DataFrame
        df = pd.DataFrame(data)

        # Sidebar filters
        st.sidebar.header("Filter Indicators")
        indicator_types = df['indicator_type'].dropna().unique().tolist()
        selected_type = st.sidebar.multiselect("Indicator Type", indicator_types, default=indicator_types)

        severities = df['severity'].dropna().unique().tolist()
        selected_severity = st.sidebar.multiselect("Severity", severities, default=severities)

        sources = df['source'].dropna().unique().tolist()
        selected_source = st.sidebar.multiselect("Source", sources, default=sources)

        # Apply filters
        filtered_df = df[
            (df['indicator_type'].isin(selected_type)) &
            (df['severity'].isin(selected_severity)) &
            (df['source'].isin(selected_source))
        ]

        # Show summary metrics
        st.markdown("### Summary")
        st.metric("Total Indicators", len(filtered_df))
        st.metric("Unique Pulses", filtered_df['pulse_id'].nunique())

        # Bar chart: Indicator Types
        st.markdown("### Indicator Types Distribution")
        st.bar_chart(filtered_df['indicator_type'].value_counts())

        # # Pie chart: Severity
        # st.markdown("### Severity Breakdown")
        # st.plotly_chart(
        #     pd.DataFrame(filtered_df['severity'].value_counts()).reset_index().rename(columns={'index': 'Severity', 'severity': 'Count'}).plot.pie(
        #         y='Count', labels='Severity', figsize=(5,5), autopct='%1.1f%%', ylabel=''),
        #     use_container_width=True
        # )
        import plotly.express as px  # Add this at the top of your script

        severity_counts = filtered_df['severity'].value_counts().reset_index()
        severity_counts.columns = ['Severity', 'Count']

        fig = px.pie(severity_counts, names='Severity', values='Count', title='Severity Breakdown')
        st.plotly_chart(fig, use_container_width=True)


        # Data Table
        st.markdown("### Raw Indicator Data")
        st.dataframe(filtered_df.reset_index(drop=True))

    except json.JSONDecodeError:
        # If JSON decoding fails
        st.error("Error: The response from the API is not valid JSON.")
        st.error(f"Raw response: {response.text}")
else:
    # Handle unsuccessful API response (non-200 status codes)
    st.error(f"Error: Failed to fetch data. Status Code: {response.status_code}")
    st.error(f"Response: {response.text}")

