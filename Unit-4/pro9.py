# Simple regex for standard email validation
email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
valid_emails = df[df['E-Mail'].str.match(email_regex, na=False)]

print("Records with valid emails:")
print(valid_emails)