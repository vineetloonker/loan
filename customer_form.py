import streamlit as st
import pandas as pd
import os
from datetime import datetime

st.set_page_config(page_title="Customer Form", page_icon="📝")

st.title("📝 Customer Entry Form")

# Input fields
name = st.text_input("Customer Name")
phone = st.text_input("Phone Number")
address = st.text_area("Address")
id_proof = st.text_input("ID Proof (Aadhar/PAN/etc.)")

# Submit Button
if st.button("Save Customer"):
    if name and phone and id_proof:
        # Prepare customer dictionary
        customer = {
            "Name": name,
            "Phone": phone,
            "Address": address,
            "ID Proof": id_proof,
            "Entry Time": datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        }

        # Save to Excel (append or create new)
        filename = "customers.xlsx"
        if os.path.exists(filename):
            df_existing = pd.read_excel(filename)
            df_new = pd.concat([df_existing, pd.DataFrame([customer])], ignore_index=True)
        else:
            df_new = pd.DataFrame([customer])

        df_new.to_excel(filename, index=False)
        st.success("✅ Customer saved successfully!")
    else:
        st.warning("Please fill all required fields (Name, Phone, ID Proof)")
