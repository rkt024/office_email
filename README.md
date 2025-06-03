# Transaction Management System

A console-based transaction management system built with Python and SQLite for managing banking transaction records with reference numbers, bank information, and dates.

## Features

- **Transaction Management**: Add, view, edit, and search transaction records
- **Reference Number Generation**: Automatically formats input numbers to RK format (e.g., RK0004651)
- **Bank Code Support**: Built-in support for 7 Nepalese banks with short codes
- **Date Validation**: Prevents future dates and validates date formats
- **Advanced Filtering**: Filter records by reference number, bank, or date
- **Reporting**: Generate various reports including date range, bank-specific, and summary reports
- **CSV Export**: Export all transaction data to CSV format
- **Data Integrity**: SQLite database with unique constraints and indexes for optimal performance

## Supported Banks

| Code | Bank Name |
|------|-----------|
| CIT  | CITIZEN INVESTMENT TRUST |
| EPF  | EMPLOYEE PROVIDENT FUND |
| GBBL | GARIMA BIKAS BANK LTD |
| MNBBL| MUKTINATH BIKASH BANK LTD |
| NIMB | NEPAL INVESTMENT MEGA BANK LTD |
| PCBL | PRIME COMMERCIAL BANK LTD |
| SADBL| SHANGRILA DEVELOPMENT BANK LTD |

## Installation

### Prerequisites
- Python 3.6 or higher
- SQLite3 (included with Python)

### Setup
1. Clone or download the script
2. No additional dependencies required - uses only Python standard library

```bash
python email.py
```

## Usage

### Main Menu Options

1. **Add Transaction**: Create new transaction records
2. **View Records**: Browse and filter existing records
3. **Edit Record**: Modify existing transaction records
4. **Generate Reports**: Create various analytical reports
5. **Export to CSV**: Export data for external use
6. **Exit**: Close the application

### Adding Transactions

1. Enter a number (e.g., 453, 4561, 10245)
2. System automatically formats it to reference number (e.g., RK0000453)
3. Select bank using short code (e.g., PCBL, GBBL)
4. Choose current date or enter custom date (YYYY-MM-DD format)

### Viewing Records

Multiple filtering options available:
- **All Records**: Display all transactions sorted by reference number
- **Filter by Reference**: Search using full or partial reference numbers
- **Filter by Bank**: Search by bank code, full name, or partial name
- **Filter by Date**: View transactions for specific dates

### Editing Records

Search for records by:
- Record ID
- Reference number
- Select from all records list

Edit any field while maintaining data integrity.

### Reports

Generate comprehensive reports:
- **Date Range Report**: Transactions within specified date range
- **Bank-specific Report**: All transactions for a particular bank
- **Reference Number Report**: Details for specific reference numbers
- **Summary Report**: Overview with statistics and recent transactions

### CSV Export

Export all transaction data to CSV format with:
- Customizable filename
- UTF-8 encoding
- Proper headers and formatting

## Database Structure

The system uses SQLite database with the following schema:

```sql
CREATE TABLE transactions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    ref_number TEXT NOT NULL UNIQUE,
    bank_name TEXT NOT NULL,
    date TEXT NOT NULL
);
```

**Indexes:**
- `idx_ref_number` on reference numbers
- `idx_date` on transaction dates

## File Structure

```
.
├── email.py                 # Main application file
├── email_records.db         # SQLite database (auto-created)
└── transactions.csv         # Exported data (when exported)
```

## Security Features

- **Input Validation**: All user inputs are validated and sanitized
- **SQL Injection Prevention**: Uses parameterized queries
- **Path Traversal Protection**: Database name validation
- **Date Validation**: Prevents future dates and invalid formats
- **Unique Constraints**: Prevents duplicate reference numbers

## Error Handling

- Database connection errors
- Invalid input formats
- Duplicate reference numbers
- File permission issues
- Invalid date formats

## Examples

### Reference Number Formatting
- Input: `453` → Output: `RK0000453`
- Input: `4561` → Output: `RK0004561`
- Input: `10245` → Output: `RK0010245`

### Bank Code Usage
- Input: `PCBL` → Resolves to: `PRIME COMMERCIAL BANK LTD`
- Input: `GBBL` → Resolves to: `GARIMA BIKAS BANK LTD`

### Date Formats
- Valid: `2024-01-15`, `2023-12-31`
- Invalid: `2025-06-01` (future date), `01-15-2024` (wrong format)

## Troubleshooting

### Common Issues

**Database Access Error:**
- Ensure write permissions in the application directory
- Check if database file is not locked by another process

**Invalid Reference Number:**
- Numbers must be between 0-9999999
- Only numeric input accepted

**Bank Code Not Found:**
- Use only supported bank codes listed above
- Check spelling and capitalization

**Date Validation Failed:**
- Use YYYY-MM-DD format
- Ensure date is not in the future
- Verify date exists (e.g., not February 30th)

### Performance Notes

- Database is optimized with indexes for fast searches
- Records are automatically sorted by reference number
- Large datasets are handled efficiently through pagination in display

## Contributing

To extend the system:
1. Add new banks to the `bank_codes` dictionary
2. Implement additional report types in the `generate_reports` method
3. Add new filtering options in the `view_records` method

## License

This project is open source. Feel free to modify and distribute according to your needs.

## Support

For issues or questions regarding the Transaction Management System, please review the troubleshooting section above or examine the source code for detailed implementation.
