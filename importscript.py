import pymysql
import csv # type: ignore
import pandas as pd
import pyreadstat

df, meta = pyreadstat.read_sav(r"C:\Users\HP\Downloads\Uganda Round 10_5 Main Survey [Fieldwork] - 31DEC24_2025_07_01_05_30\Uganda Round 10_5 Main Survey [Fieldwork] - 31DEC24_2025_07_01_05_30.sav")

# Convert the date column (assuming it's named 'date_column') to the correct format
df['Date'] = pd.to_datetime(df['Date'], format='%d-%b-%Y  %H:%M:%S')

# Database connection
connection = pymysql.connect(
    host="localhost",
    user="root",
    password="mAk_Octane123*$",
    database="survey_data"
)

try:

    # # Open CSV file
    # with open("H:\\ProgramData\\MySQL\\MySQL Server 8.3\\Uploads\\Uganda Round 10_5 Main Survey (Fieldwork) - 31DEC24_2025_03_01_04_24.csv", "r") as file:
    #     csv_data = csv.DictReader(file)
    #     next(csv_data)  # Skip header row

        # Insert data into MySQL
        cursor = connection.cursor()
        for index, row in df.iterrows():

            # for index, row in df.iterrows():
            #     # Extract only the required columns
            #     date = row["Date"]
            #     EANUMB = row["EANUMB"]
            #     Srvyr = row["Srvyr"]

            cursor.execute(
                "INSERT INTO survey_results (date, EANUMB, Srvyr) VALUES (%s, %s, %s)",
                (row["Date"], row["EANUMB"], row["Srvyr"])
            )

        connection.commit()
        print("Data imported successfully!")

except Exception as e:
    print(f"Error: {e}")

finally:
    cursor.close()
    connection.close()
