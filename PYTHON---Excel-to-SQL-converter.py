import pandas as pd
import sqlite3
from pathlib import Path

def excel_to_sql(excel_file, db_name):
    try:
        # Check if the file exists
        excel_path = Path(excel_file)
        if not excel_path.is_file():
            print("Excel file not found!")
            return
        
        # Read Excel file
        excel_data = pd.ExcelFile(excel_file)
        print(f"Found sheets: {excel_data.sheet_names}")
        
        # Connect to SQLite database (or create one if it doesn't exist)
        conn = sqlite3.connect(db_name)
        print(f"Connected to database: {db_name}")
        
        # Iterate through each sheet and save it as a table
        for sheet_name in excel_data.sheet_names:
            df = excel_data.parse(sheet_name)
            table_name = sheet_name.replace(" ", "_")  # Replace spaces with underscores
            df.to_sql(table_name, conn, if_exists='replace', index=False)
            print(f"Imported sheet '{sheet_name}' as table '{table_name}'")
        
        # Close connection
        conn.close()
        print(f"Database '{db_name}' created successfully!")
    
    except Exception as e:
        print(f"An error occurred: {e}")

# Example Usage
excel_file = "example.xlsx"  # Replace with your Excel file path
db_name = "example.db"  # Desired database name
excel_to_sql(excel_file, db_name)
