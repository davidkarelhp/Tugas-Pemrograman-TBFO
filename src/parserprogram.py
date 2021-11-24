import readCNF
import token
import fa
import sys


def cyk(inputToken, non_terminals, terminals, CNFgrammar):
    n = len(inputToken)
    if (n == 0):
        print("Accepted")
        return True
    else:
        table = [[set() for j in range(n)] for i in range(n)]
        array = []
        singleQuote = True
        doubleQuote = True
        for i in range(n):
            for key in CNFgrammar:
                for j in range(len(CNFgrammar[key])):
                    if (len(CNFgrammar[key][j]) == 1 and CNFgrammar[key][j][0] == inputToken[i]):
                        table[i][i].add(key)
            if not (inputToken[i] in terminals):
                table[i][i].add("EXPRESSION")

            # Tidak membaca komen dan string
            if (inputToken[i] == "'"):
                singleQuote = not singleQuote
            if (inputToken[i] == '"'):
                doubleQuote = not doubleQuote
    
            if singleQuote and doubleQuote and ((not (inputToken[i] in terminals)) or inputToken[i] == "pass" or inputToken[i] == "break" or inputToken[i] == "continue" or inputToken[i] == "None" or inputToken[i] == "True" or inputToken[i] == "False"):
                array.append(inputToken[i])
            else:
                if (len(array) != 0):
                    cekFiniteAutomata = fa.fa(array)
                    if (not cekFiniteAutomata):
                        print("Syntax Error")
                        return False                    
                array = []

        if (len(array) != 0):
            # print(array)
            cekFiniteAutomata = fa.fa(array)
            if (not cekFiniteAutomata):
                print("Syntax Error")
                return False

        check = True
        for i in range(n):
                if not ("EXPRESSION" in table[i][i] or "BOOLEAN" in table[i][i]):
                    check = False
                    break
        if (check):
            print("Accepted")
            return True

        # count = 0
        accepted = False
        for l in range(1, n + 1):
            for i in range(n - l + 1):
                j = i + l - 1
                for k in range(i, j):
                    for key in CNFgrammar:
                        for x in range(len(CNFgrammar[key])):
                            # count += 1
                            if (len(CNFgrammar[key][x]) == 2):
                                if (CNFgrammar[key][x][0] in table[i][k] and CNFgrammar[key][x][1] in table[k + 1][j]):
                                        table[i][j].add(key)
                            if (i == 0 and j == n - 1 and "S" in table[0][n - 1]):
                                accepted = True
                                break
                        if (accepted):
                            break
                    if (accepted):
                        break                               
        if (accepted):
            print("Accepted")
        else:
            print("Syntax Error")
        return accepted

def main():
    non_terminals, terminals, CNFgrammar = readCNF.readCNF(r"./grammar/CNF.txt")
    inputToken = token.tokenizeInput('./' + sys.argv[1])
    cyk(inputToken, non_terminals, terminals, CNFgrammar)

if __name__ == "__main__":
    main()