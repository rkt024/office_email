import sqlite3
import csv

# Function to import CSV data into SQLite database
def import_csv_to_db(csv_file, db_file):
    # Connect to the SQLite database (it will create the file if it doesn't exist)
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()

    # Open the CSV file
    with open(csv_file, 'r') as file:
        # Create a CSV reader
        csv_reader = csv.DictReader(file)

        # Prepare SQL query for inserting data
        insert_query = '''INSERT INTO transactions (ref_number, bank_name, date)
                          VALUES (?, ?, ?)'''

        # Initialize a counter for inserted rows
        inserted_count = 0

        # Loop through CSV rows and insert data into the database
        for row in csv_reader:
            # Extract the data from each row
            ref_number = row['ref_number']
            bank_name = row['bank_name']
            date = row['date']

            # Execute the insert query
            cursor.execute(insert_query, (ref_number, bank_name, date))
            inserted_count += 1  # Increment the counter

    # Commit changes and close the connection
    conn.commit()

    # Query to count the total number of rows in the table
    cursor.execute("SELECT COUNT(*) FROM transactions")
    total_rows = cursor.fetchone()[0]  # Fetch the result of the COUNT query

    conn.close()

    # Print the results
    print(f"Data from {csv_file} has been successfully imported into {db_file}.")
    print(f"{inserted_count} rows were inserted.")
    print(f"Total rows in the database: {total_rows}")

# Usage
csv_file = 'transactions.csv'  # Path to your CSV file
db_file = 'database.db'        # Path to your SQLite database file

import_csv_to_db(csv_file, db_file)