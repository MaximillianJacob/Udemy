import email

def parse_email(file_path):
    """
    Parses an email file and extracts its headers and body content.

    Args:
        file_path (str): The path to the email file to be parsed.

    Prints:
        - The "From" header of the email.
        - The "To" header of the email.
        - The "Subject" header of the email.
        - The plain text body of the email, if available.
        - The HTML body of the email, if available.

    Notes:
        - If the email is multipart, it iterates through its parts to extract
          the plain text and HTML content separately.
        - If the email is not multipart, it directly extracts the payload as
          both plain text and HTML.
    """
    # Open the email file in read mode
    with open(file_path, 'r') as file:
        # Parse the email file into a message object
        msg = email.message_from_file(file)
        # Print the "From" header of the email
        print("From:", msg['From'])
        # Print the "To" header of the email
        print("To:", msg['To'])
        # Print the "Subject" header of the email
        print("Subject:", msg['Subject'])

    # Check if the email is multipart
    if msg.is_multipart():
        # Iterate through each part of the multipart email
        for part in msg.walk():
            # Check if the part is plain text
            if part.get_content_type() == 'text/plain':
                # Decode and print the plain text body
                print("Body:", part.get_payload(decode=True).decode())
            # Check if the part is HTML
            elif part.get_content_type() == 'text/html':
                # Decode and print the HTML body
                print("HTML Body:", part.get_payload(decode=True).decode())
    else:
        # If the email is not multipart, decode and print the plain text body
        print("Body:", msg.get_payload(decode=True).decode())
        # Decode and print the HTML body (if applicable)
        print("HTML Body:", msg.get_payload(decode=True).decode())

    # q: What does the with open... does?
    # a: The `with open(file_path, 'r') as file:` statement opens the specified
    #    file in read mode ('r') and assigns it to the variable `file`. The
    #    `with` statement ensures that the file is properly closed after its
    #    suite finishes, even if an exception is raised. This is a context
    #    manager that handles the opening and closing of the file automatically.
    with open(file_path, 'r') as file:
        msg = email.message_from_file(file)
        print("From:", msg['From'])
        print("To:", msg['To'])
        print("Subject:", msg['Subject'])

    if msg.is_multipart():
        for part in msg.walk():
            if part.get_content_type() == 'text/plain':
                print("Body:", part.get_payload(decode=True).decode())
            elif part.get_content_type() == 'text/html':
                print("HTML Body:", part.get_payload(decode=True).decode())
    else:
        print("Body:", msg.get_payload(decode=True).decode())
        print("HTML Body:", msg.get_payload(decode=True).decode())
if __name__ == "__main__":
    print("Running email_parser.py as a standalone script...")
    print("Max rules")
    print("Agent Max testing")
    import sys
    if len(sys.argv) != 2:
        print("Usage: python email_parser.py <email_file>")
        sys.exit(1)
    parse_email(sys.argv[1])
