import streamlit as st
import gspread
import json
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime

# ✅ Use credentials from Streamlit secrets (not from file)
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds_dict = json.loads(st.secrets["credentials"])
creds = ServiceAccountCredentials.from_json_keyfile_dict(creds_dict, scope)
client = gspread.authorize(creds)

# Access sheet
sheet = client.open_by_key(st.secrets["sheet_id"]).sheet1

# UI - Customer Form
st.set_page_config(page_title="Customer Form", page_icon="📝")
st.title("📝 Customer Entry Form")

name = st.text_input("Customer Name")
phone = st.text_input("Phone Number")
address = st.text_area("Address")
id_proof = st.text_input("ID Proof (Aadhar/PAN/etc.)")

if st.button("Save Customer"):
    if len(name.strip()) > 0 and len(phone.strip()) > 0 and len(id_proof.strip()) > 0:
        new_row = [name, phone, address, id_proof, datetime.now().strftime("%d-%m-%Y %H:%M:%S")]
        sheet.append_row(new_row)
        st.success("✅ Customer saved to Google Sheet!")
    else:
        st.warning("Please fill all required fields.")
