# Regex for 2-digit country code, hyphen, and 10-digit number (91-9999933333)
mobile_regex = r'^\d{2}-\d{10}$'
valid_mobile = df[df['Mobile'].str.match(mobile_regex, na=False)]

print("Records with valid country code mobile numbers:")
print(valid_mobile)