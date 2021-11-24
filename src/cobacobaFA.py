
def varCheck(word):
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    correct = False
    if word == "True":
        datatype = "NONASSIGN"
        correct = True
    elif word == "False":
        datatype = "NONASSIGN"
        correct = True
    elif word == "None":
        datatype = "NONASSIGN"
        correct = True
    
    elif word == "+=":
        datatype = "ASSIGN"
        correct = True
    elif word == "-=":
        datatype = "ASSIGN"
        correct = True
    elif word == "**=":
        datatype = "ASSIGN"
        correct = True
    elif word == "*=":
        datatype = "ASSIGN"
        correct = True
    elif word == "//=":
        datatype = "ASSIGN"
        correct = True
    elif word == "/=":
        datatype = "ASSIGN"
        correct = True
    elif word == "=":
        datatype = "REPEATASSIGN"
        correct = True
    
    elif word == "+":
        datatype = "OPERATORS"
        correct = True
    elif word == "-":
        datatype = "OPERATORS"
        correct = True
    elif word == "**":
        datatype = "OPERATORS"
        correct = True
    elif word == "*":
        datatype = "OPERATORS"
        correct = True
    elif word == "//":
        datatype = "OPERATORS"
        correct = True
    elif word == "/":
        datatype = "OPERATORS"
        correct = True
    
    elif word == ">=":
        datatype = "RELATIONS"
        correct = True
    elif word == ">":
        datatype = "RELATIONS"
        correct = True
    elif word == "<=":
        datatype = "RELATIONS"
        correct = True
    elif word == "<":
        datatype = "RELATIONS"
        correct = True
    elif word == "==":
        datatype = "RELATIONS"
        correct = True
    
    elif not(word[0] in numbers):
        datatype = "VARIABLES"
        correct = True

    return correct, datatype
    