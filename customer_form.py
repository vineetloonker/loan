import streamlit as st
from datetime import datetime
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Setup Google Sheets API
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("loan-app-463017.json", scope)
client = gspread.authorize(creds)

# Open the worksheet
st.write("Using sheet_id:", st.secrets.get("sheet_id"))
sheet = client.open_by_key(st.secrets["sheet_id"]).sheet1

# Page setup
st.set_page_config(page_title="Customer Form", page_icon="📝")
st.title("📝 Customer Entry Form")

# Input fields
name = st.text_input("Customer Name")
phone = st.text_input("Phone Number")
address = st.text_area("Address")
id_proof = st.text_input("ID Proof (Aadhar/PAN/etc.)")

# Submit button
if st.button("Save Customer"):
    if len(name.strip()) > 0 and len(phone.strip()) > 0 and len(id_proof.strip()) > 0:
        new_row = [name, phone, address, id_proof, datetime.now().strftime("%d-%m-%Y %H:%M:%S")]
        sheet.append_row(new_row)
        st.success("✅ Customer saved to Google Sheet!")
    else:
        st.warning("Please fill all required fields.")
