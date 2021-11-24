
def varCheck(word):
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    correct = False
    datatype = "REJECT"
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
    
    elif ((ord(word[0]) > 64 and ord(word[0]) < 91) or (ord(word[0]) == 95) or (ord(word[0]) > 96 and ord(word[0]) < 123)):
        datatype = "VARIABLES"
        correct = True

    else:
        angka = True
        for huruf in word:
            if not(huruf in numbers):
                angka = False
                break
        if(angka):
            datatype = "NONASSIGN"
            correct = True

    return correct, datatype
    
    