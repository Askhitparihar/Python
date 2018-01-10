import re

str = "Cats are smarter than dogs"

matchObj = re.match(r'(.*) are (.*?) .*', str, re.M|re.I)

if matchObj:
    print("matchObj.group():", matchObj.group())
    print("matchObj.group(1):", matchObj.group(1))
    print("matchObj.group(2):", matchObj.group(2))
else:
    print("No match!")
    
"""
    example - re.match(pattern, string, flags=0)
    pattern - This is the regular expression to be matched.
    string - This is the string, which would be searched to match the pattern at the beginning of string.
    flags - Specify different flags using bitwise OR (|). These are modifiers, which are listed in the table below.
     
    group(num = 0) - This method returns entire match (or specific subgroup num)
    groups() - This method returns all matching subgroups in a tuple ("None" if there weren't any matches).
"""