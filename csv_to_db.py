import sqlite3
import csv
import os

def import_csv_to_db(csv_file, db_file):
    # Validate input files
    if not os.path.isfile(csv_file):
        print(f"Error: CSV file '{csv_file}' does not exist.")
        return
    if not db_file:
        print("Error: Database file path cannot be empty.")
        return

    inserted_count = 0
    failed_count = 0
    total_rows = 0

    try:
        # Connect to the database using context manager
        with sqlite3.connect(db_file) as conn:
            conn.execute("PRAGMA foreign_keys = ON")
            cursor = conn.cursor()
            
            # Create table if not exists
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS transactions (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    ref_number TEXT,
                    bank_name TEXT NOT NULL,
                    date TEXT NOT NULL
                )
            ''')
            
            # Open CSV file
            with open(csv_file, 'r') as file:
                csv_reader = csv.DictReader(file)
                
                if not all(col in csv_reader.fieldnames for col in ['ref_number', 'bank_name', 'date']):
                    print("Error: CSV file is missing required columns")
                    return
                
                # Process each row
                for row in csv_reader:
                    try:
                        # Validate required fields
                        if not all(row.get(col) for col in ['ref_number', 'bank_name', 'date']):
                            raise ValueError("Missing required field(s)")
                            
                        # Prepare data
                        ref_number = row['ref_number'].strip()
                        bank_name = row['bank_name'].strip()
                        date = row['date'].strip()
                        
                        # Insert record
                        cursor.execute(
                            '''INSERT INTO transactions (ref_number, bank_name, date)
                               VALUES (?, ?, ?)''',
                            (ref_number, bank_name, date)
                        )
                        inserted_count += 1
                        
                    except (ValueError, KeyError) as e:
                        print(f"Data error in row: {row} - {str(e)}")
                        failed_count += 1
                    except sqlite3.IntegrityError as e:
                        print(f"Duplicate ref_number '{ref_number}' - {str(e)}")
                        failed_count += 1
                    except sqlite3.Error as e:
                        print(f"Database error on row: {row} - {str(e)}")
                        failed_count += 1
                    except Exception as e:
                        print(f"Unexpected error on row: {row} - {str(e)}")
                        failed_count += 1
                
                # Get total rows after insertion
                cursor.execute("SELECT COUNT(*) FROM transactions")
                total_rows = cursor.fetchone()[0]
                
    except sqlite3.Error as e:
        print(f"Database connection error: {str(e)}")
        return
    except (IOError, OSError) as e:
        print(f"File I/O error: {str(e)}")
        return
    except csv.Error as e:
        print(f"CSV parsing error: {str(e)}")
        return
    except Exception as e:
        print(f"Unexpected error: {str(e)}")
        return

    # Print summary
    print(f"Import completed: {inserted_count} rows inserted, {failed_count} rows failed")
    print(f"Total rows in database: {total_rows}")

# Usage
if __name__ == "__main__":
    csv_file = 'email_records.csv'
    db_file = 'email_records.db'
    import_csv_to_db(csv_file, db_file)
