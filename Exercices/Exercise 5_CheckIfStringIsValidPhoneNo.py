import re

phone = "234-4563-999"
pattern = r'^\d{3}[-\s]?\d{3}[-\s]?\d{4}$'

if (re.match(pattern,phone)):
    print(f"{phone} is a valid 10 digit phone number")
else:
    print(f"{phone} is not a valid 10 digit phone number")
