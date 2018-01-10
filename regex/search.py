import re

str = "Cats are smarter than dogs"

searchObj = re.search(r'(.*) are (.*?) .*', str, re.M|re.I)

if searchObj:
    print("searchObj.group():", searchObj.group())
    print("searchObj.group(1):", searchObj.group(1))
    print("searchObj.group(2):", searchObj.group(2))
else:
    print("Nothing found!")
    
"""
    example - re.search(pattern, string, flags=0)
    pattern - This is the regular expression to be matched.
    String - This is the string, which would be searched to match the pattern anywhere in the string.
    flags - Specify different flags using bitwise OR (|). These are modifiers, which are listed in the table below.

    group(num=0) - This method returns entire match (or specific subgroup num)
    groups() - This method returns all matching subgroups in a tuple (empty if there weren't any)
"""