import streamlit as st
from datetime import datetime
import gspread
from oauth2client.service_account import ServiceAccountCredentials

st.set_page_config(page_title="Customer Form", page_icon="📝")
st.title("📝 Customer Entry Form")

# Input fields
name = st.text_input("Customer Name")
phone = st.text_input("Phone Number")
address = st.text_area("Address")
id_proof = st.text_input("ID Proof (Aadhar/PAN/etc.)")

# Save button
if st.button("Save Customer"):
    if len(name.strip()) > 0 and len(phone.strip()) > 0 and len(id_proof.strip()) > 0:
        try:
            # Google Sheets setup
            scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
            creds = ServiceAccountCredentials.from_json_keyfile_dict(st.secrets["gcp_service_account"], scope)
            client = gspread.authorize(creds)

            sheet = client.open_by_key(st.secrets["sheet_id"]).worksheet("Sheet1")
            new_row = [name, phone, address, id_proof, datetime.now().strftime("%d-%m-%Y %H:%M:%S")]
            sheet.append_row(new_row)

            st.success("✅ Customer saved to Google Sheet!")

        except Exception as e:
            st.error(f"Error: {e}")
    else:
        st.warning("Please fill all required fields (Name, Phone, ID Proof)")
