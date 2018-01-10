import re

phone = "2004-959-559 # This is a Phone Number"

# Delete Python-style comments
num = re.sub(r'#.*$', "", phone)
print("Phone number: ", num)

# Remove anything other than digits
num = re.sub(r'\D', "", phone)
print("Phone number: ", num)