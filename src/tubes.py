
def printTable(t):
    for  i in range(len(t)):
        for j in range(len(t[0])):
            print(t[i][j], end='')
        print()
from abc import abstractmethod
# from os import WCOREDUMP
# from src.token import tokenizeInput
import readCNF
import token
import os

# print(os.getcwd())

# David
non_terminals, terminals, CNFgrammar = readCNF.readCNF(r".\src\grammar\CNF.txt")

# Brian
# non_terminals, terminals, CNFgrammar = readCNF.readCNF(r"./grammar/CNF.txt")


# print(CNFgrammar)
# print(terminals)

def cyk(word):
    n = len(word)
    table = [[set() for j in range(n)] for i in range(n)]
    for i in range(n):
        for key in CNFgrammar:
            for j in range(len(CNFgrammar[key])):
                if (len(CNFgrammar[key][j]) == 1 and CNFgrammar[key][j][0] == word[i]):
                    table[i][i].add(key)
                if not (word[i] in terminals):
                    table[i][i].add("EXPRESSION")
    # printTable(table)

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
    print(table[0][n - 1])
    # print(count)
    if (accepted):
        print("accepted")
    else:
        print("rejected")
    return accepted

# word = "(((((e))))(e)((e)))"

# David
word = token.tokenizeInput(r'.\src\tes.txt')

# Brian
# word = token.tokenizeInput('./tes.txt')
# print(word)

# print(word)

cyk(word)
# printTable(table)