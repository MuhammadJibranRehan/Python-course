# Imports
import streamlit as st
import pandas as pd
import os
from io import BytesIO
from xlsxwriter import Workbook


# Main working of app
st.set_page_config(page_title="Data Sweeper", layout="wide")
st.title("🧹 Data Sweeper")
st.write("Transform your files between CSV and Excel formats with built-in data cleaning and visualization!")

uploaded_files = st.file_uploader("Upload a file (CSV or EXCEL format)", type=["csv", "xlsx"], accept_multiple_files=True)

if uploaded_files:
    for file in uploaded_files:
        file_ext = os.path.splitext(file.name)[-1].lower()

        # Read File
        try:
            if file_ext == ".csv":
                df = pd.read_csv(file)
            elif file_ext == ".xlsx":
                df = pd.read_excel(file, engine="openpyxl")
            else:
                st.error(f"Unsupported file format: {file_ext}")
                continue
        except Exception as e:
            st.error(f"Error reading file {file.name}: {str(e)}")
            continue

        # Display File Information
        file_size_kb = len(file.getvalue()) / 1024  # Calculate file size in KB
        st.write(f"**File Name:** {file.name}")
        st.write(f"**File Size:** {file_size_kb:.2f} KB")

        # Display Data Preview
        st.write("## Data Preview")
        st.write(df.head())

        # Data Cleaning Options
        st.subheader("🛠 Data Cleaning Options")
        col1, col2 = st.columns(2)

        with col1:
            if st.button(f"Remove Duplicates from {file.name}"):
                df.drop_duplicates(inplace=True)
                st.success("✅ Duplicates removed successfully!")

        with col2:
            if st.button(f"Fill Missing Values for {file.name}"):
                numeric_cols = df.select_dtypes(include=['number']).columns
                df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())
                st.success("✅ Missing values filled successfully!")

        # Column Selection
        st.subheader("📌 Select Columns to Keep")
        selected_columns = st.multiselect(f"Choose columns for {file.name}", df.columns, default=df.columns)
        if selected_columns:
            df = df[selected_columns]

        # Data Visualization
        st.subheader("📊 Data Visualization")
        if st.checkbox(f"Show Visualizations for {file.name}"):
            # First, check for numeric columns in the current dataframe
            numeric_cols = df.select_dtypes(include='number').columns

            if numeric_cols.empty:
                # Attempt to convert each column to numeric if possible
                converted_df = df.copy()
                for col in converted_df.columns:
                    converted_df[col] = pd.to_numeric(converted_df[col], errors='coerce')
                numeric_cols = converted_df.select_dtypes(include='number').columns

                if numeric_cols.empty:
                    st.warning("⚠️ No numeric columns available for visualization even after conversion.")
                else:
                    st.bar_chart(converted_df[numeric_cols].iloc[:, :2])
            else:
                st.bar_chart(df[numeric_cols].iloc[:, :2])

        # File Conversion Options
        st.subheader("🔄 File Conversion")
        conversion_type = st.radio(f"Convert {file.name} to:", ["CSV", "Excel"], key=file.name)
        if st.button(f"Convert {file.name} to {conversion_type}"):
            buffer = BytesIO()

            if conversion_type == "CSV":
                df.to_csv(buffer, index=False)
                file_name = file.name.replace(file_ext, ".csv")
                mime_type = "text/csv"
            else:  # Excel conversion
                with pd.ExcelWriter(buffer, engine="xlsxwriter") as writer:
                    df.to_excel(writer, index=False)
                file_name = file.name.replace(file_ext, ".xlsx")
                mime_type = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"

            buffer.seek(0)

            # Download Button
            st.download_button(
                label=f"⬇️ Download {file.name} as {conversion_type}",
                data=buffer,
                file_name=file_name,
                mime=mime_type
            )
            st.success("🏆 File converted successfully!")

