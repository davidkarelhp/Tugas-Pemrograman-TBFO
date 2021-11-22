import readCNF

non_terminals, terminals, CNFgrammar = readCNF.readCNF(r".\CNF.txt")
print(CNFgrammar)

def cyk(word):
    n = len(word)
    table = [[set() for j in range(n)] for i in range(n)]
    for i in range(n):
        for key in CNFgrammar:
            for j in range(len(CNFgrammar[key])):
                if (len(CNFgrammar[key][j]) == 1 and CNFgrammar[key][j][0] == word[i]):
                    table[i][i].add(key)

    # count = 0
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
                            break
                    if (i == 0 and j == n - 1 and "S" in table[0][n - 1]):
                        break
                if (i == 0 and j == n - 1 and "S" in table[0][n - 1]):
                    break                               

    # print(count)
    if ("S" in table[0][n - 1]):
        print("accepted")
    else:
        print("rejected")
    return "S" in table[0][n - 1]

word = "(((((e))))(e)((e)))"
cyk(word)

def printTable(t):
    for  i in range(len(t)):
        for j in range(len(t[0])):
            print(t[i][j], end='')
        print()

# printTable(table)