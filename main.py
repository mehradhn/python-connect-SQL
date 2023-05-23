import pyodbc
from datetime import datetime

# Connect to the SQL Server database
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=DESKTOP-T5KNQ7J;'
                      'Database=mhn;'
                      'Trusted_Connection=yes;')

# Create a cursor object to execute SQL queries
cursor = conn.cursor()

# Generate and execute the SQL insert statements
for i in range(10000):
    row_id = i
    identifier = i
    status = 0
    issuing_center = f'issuing_center_{i}'
    profile = f'profile_{i}'
    program = f'program_{i}'
    request_date = datetime.strptime('09-19-2022', '%m-%d-%Y').date()
    
    issuance_date =datetime.strptime('09-19-2022', '%m-%d-%Y').date()
    expiration_date = datetime.strptime('09-19-2025', '%m-%d-%Y').date()
    cancellation_date = datetime.strptime('09-19-2028', '%m-%d-%Y').date()
    tracking_code = f'tracking_code_{i}'

    sql_insert = f"INSERT INTO pendar (Row_id, Identifier, Status, Issuing_center, Profile, ProgramName, " \
                 f"Request_date, Issuance_date, Expiration_date, Cancellation_date, Tracking_code) " \
                 f"VALUES ({row_id}, '{identifier}', '{status}', '{issuing_center}', '{profile}', '{program}', " \
                 f"'{request_date}', '{issuance_date}', '{expiration_date}', '{cancellation_date}', " \
                 f"'{tracking_code}')"

    cursor.execute(sql_insert)

# Commit the changes and close the connection
conn.commit()
conn.close()
