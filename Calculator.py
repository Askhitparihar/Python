import re

# Program to create a simple calculator using Regex and eval functionality #
print("===============Calculator===============")
print("Type 'quit' to stop program from running.\n")

previous = 0
run = True

def performMath():
    global run
    global previous
    equation = ''
    if previous == 0:
        # for python2.7 use raw_input() - python3+ use input() #
        equation = raw_input("Enter equation: ")
    else:
        equation = raw_input("Enter Equation: " + str(previous))

    if equation == "quit":
        print("Goodbye!")
        run = False
    else:
        equation = re.sub('[a-zA-Z,.:()" "]', '', equation)
        if previous == 0:
            previous = eval(equation)
        else:
            previous = eval(str(previous) + equation)

while run:
    performMath()