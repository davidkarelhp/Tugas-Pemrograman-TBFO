# from os import WCOREDUMP
# from src.token import tokenizeInput
import readCNF
import token
import os
# print(os.getcwd())
non_terminals, terminals, CNFgrammar = readCNF.readCNF(r".\src\grammar\CNF.txt")
# CNFgrammar ={
#     'S': [["e"], ["C", "B"]],
#     "A": [["("]],
#     "B": [[")"]],
#     "C": [["A", 'S']]
# }
# print(CNFgrammar)

def printTable(t):
    for  i in range(len(t)):
        for j in range(len(t[0])):
            print(t[i][j], end='')
        print()

def cyk(word):
    n = len(word)
    table = [[set() for j in range(n)] for i in range(n)]
    for i in range(n):
        # print(word[i])
        for key in CNFgrammar:
            for j in range(len(CNFgrammar[key])):
                if (len(CNFgrammar[key][j]) == 1 and CNFgrammar[key][j][0] == word[i]):
                    table[i][i].add(key)
    # printTable(table)

    # count = 0
    for l in range(1, n + 1):
        for i in range(n - l + 1):
            j = i + l - 1
            for k in range(i, j):
                for key in CNFgrammar:
                    for x in range(len(CNFgrammar[key])):
                        # count += 1
                        # print(count)
                        if (len(CNFgrammar[key][x]) == 2):
                            # print(CNFgrammar[key][x][0])
                            # print(CNFgrammar[key][x][1])
                            if (CNFgrammar[key][x][0] in table[i][k] and CNFgrammar[key][x][1] in table[k + 1][j]):
                                    table[i][j].add(key)
                        if (i == 0 and j == n - 1 and "S" in table[0][n - 1]):
                            break
                    if (i == 0 and j == n - 1 and "S" in table[0][n - 1]):
                        break
                if (i == 0 and j == n - 1 and "S" in table[0][n - 1]):
                    break                               

    # print(count)
    # printTable(table)
    if ("S" in table[0][n - 1]):
        print("accepted")
    else:
        print("rejected")
    return "S" in table[0][n - 1]

# word = "(((((e))))(e)((e)))"
word = token.tokenizeInput(r'.\src\tes2.txt')
# print(word)
cyk(word)
# cyk(word)

# printTable(table)
for i in range(10):
    def brian(x):
        pass