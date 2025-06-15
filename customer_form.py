import json
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import streamlit as st

scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]

# Load service account from secrets
creds_dict = json.loads(st.secrets["credentials"])
creds = ServiceAccountCredentials.from_json_keyfile_dict(creds_dict, scope)
client = gspread.authorize(creds)

# Open your Google Sheet
sheet = client.open_by_key(st.secrets["sheet_id"]).sheet1
