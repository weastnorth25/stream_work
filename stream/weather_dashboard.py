import pandas as pd
import streamlit as st
import requests



API_KEY = "CWA-9DE1DB1A-8936-4A81-AEE0-F457BFA159F0"
st.title("🌧️ 台灣氣象資料 Dashboard")

LOCATION_OPTIONS = ["Taipei", "Taichung", "Kaohsiung"]
LOCATION = st.selectbox("選擇城市", LOCATION_OPTIONS)

url = f"https://opendata.cwa.gov.tw/api/v1/rest/datastore/F-C0032-001?Authorization={API_KEY}&locationName={LOCATION}"


res = requests.get(url)

data = res.json()
location = data["records"]["location"][0]
st.subheader(f"📍 {location['locationName']} 36 小時預報")

for element in location["weatherElement"]:
        name = element["elementName"]
        value = element["time"][0]["parameter"][0]["parameterName"]

        st.write(f"**{name}**: {value}")
