import re

str = "Cats are smarter than dogs"

matchObj = re.match(r'dogs', str, re.M|re.I)

if matchObj:
    print("Match --> matchObj.group():", matchObj.group())
else:
    print("No match!")
    
searchObj = re.search(r'dogs',str,re.M|re.I)
if searchObj:
    print("Search --> searchObj.group():", searchObj.group())
else:
    print("Nothing found!")