
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
    
def parsingLine(array):
    correct = True
    urutan = []
    datatype = "REJECT"
    lenght = len(array)
    i = 0
    while(i < lenght):
        # checking pasangan tiga
        if((array[i] == "*" or array[i] == "/") and i+2 < lenght):
            if(array[i] == "*"):
                if(array[i+1] == "*"):
                    if(array[i+2] == "="):
                        datatype = "ASSIGN"
                        i += 3
            if(array[i] == "/"):
                if(array[i+1] == "/"):
                    if(array[i+2] == "="):
                        datatype = "ASSIGN"
                        i += 3
            
        # checking pasangan dua
        if((array[i] == "+" or array[i] == "-" or array[i] == "*" or array[i] == "/" or array[i] == "<" or array[i] == ">" or array[i] == "=") and i+1 <= lenght):
            if(array[i] == "+"):
                if(array[i+1] == "="):
                    datatype = "ASSIGN"
                    i += 2
            elif(array[i] == "-"):
                if(array[i+1] == "="):
                    datatype = "ASSIGN"
                    i += 2
            elif(array[i] == "*"):
                if(array[i+1] == "="):
                    datatype = "ASSIGN"
                    i += 2
            elif(array[i] == "/"):
                if(array[i+1] == "="):
                    datatype = "ASSIGN"
                    i += 2
            elif(array[i] == "<"):
                if(array[i+1] == "="):
                    datatype = "RELATIONS"
                    i += 2
            elif(array[i] == ">"):
                if(array[i+1] == "="):
                    datatype = "RELATIONS"
                    i += 2
            elif(array[i] == "="):
                if(array[i+1] == "="):
                    datatype = "RELATIONS"
                    i += 2

        if (datatype == "REJECT"):
            correct, datatype = varCheck(array[i])
            i += 1
        if(not correct):
            return False
        else:
            urutan.append(datatype)

    panjangurut = len(urutan)
    if(panjangurut > 2):
        i = 2
        if(urutan[0] != "VARIABLES" or urutan[1] == "VARIABLES" or urutan[1] == "NONASSIGN"):
            return False
        if(urutan[1] == "OPERATOR" or urutan[1] == "ASSIGN" or urutan[1] == "RELATIONS"):
            if panjangurut == 3:
                return (urutan[2] == "VARIABLES" or urutan[2] == "NONASSIGN")
            else:
                return False
        else:
            ulang = True
            while (i < panjangurut and ulang):
                if(i%2 == 0):
                    ulang = (urutan[i] == "VARIABLES" or urutan[i] == "NONASSIGN")
                else:
                    ulang = urutan[i] == "REPEATASSIGN"
            return ulang
                    
    elif (panjangurut == 1):
        return (urutan[0] == "VARIABLES" or urutan[0] == "NONASSIGN")
    else:
        return False
                
