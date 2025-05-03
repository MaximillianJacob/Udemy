# Email Parser Project

This project provides a simple Python script to parse `.eml` email files and extract their headers and body content.

## Files in the Workspace

### 1. `email_parser.py`
This is the main Python script that parses email files. It includes the following features:
- Extracts and prints the "From", "To", and "Subject" headers of the email.
- Extracts and prints the plain text and HTML body of the email.
- Handles both multipart and non-multipart email formats.

#### Usage:
Run the script from the command line with the path to the email file as an argument:
```bash
python  <email_file>