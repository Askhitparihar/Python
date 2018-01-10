import re

print("Search:")
regex = r"([a-zA-Z]+) (\d+)"
match = re.search(regex, "June 24")
if match is not None:
    print("Match at index", match.start(), match.end())
    print("Full match:", match.group())
    print("Day:", match.group(2))
else:
    print("The regex pattern does not match.")
    
print()    

print("Findall:")
print("Match date strings full")
regex = r"[a-zA-Z]+ \d+"
matches = re.findall(regex, "June 24, August 9, Dec 12")
for match in matches:
    print("Full Match:",match)
    
print("Match date strings month")
regex = r"([a-zA-Z]+) \d+"
matches = re.findall(regex, "June 24, August 9, Dec 12")
for match in matches:
    print("Match Month:", match)
    
print("Match date positions in strings")
regex = r"([a-zA-Z]+) \d+"
matches = re.finditer(regex, "June 24, August 9, Dec 12")
for match in matches:
    print("Match at index:", match.start(), match.end())
    
print()

print("Replace:")
regex = r"([a-zA-Z]+) (\d+)"
print (re.sub(regex, r"\2 of \1", "June 24, August 9, Dec 12"))

print()
print("Compile:")
regex = re.compile(r"(\w+) World")
result = regex.search("Hello World is the easiest.")
if result:
    print(result.start(), result.end())
for result in regex.findall("Hello World, Bonjour World"):
    print(result)
print(regex.sub(r"\1 Earth", "Hello World"))