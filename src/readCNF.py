def readCNF(CNFpath):
    file = open(CNFpath).read()
    grammars = file.split('\n')
    non_terminals = []
    terminals = []
    R = {}
    
    for grammar in grammars:
        left, right = grammar.split(" -> ")
        
        if left not in non_terminals:
            non_terminals.append(left)
            R[left] = []

        right = right.split(" | ")
        for ri in right:
            r = ri.split()
            if (len(r) == 1):
                if r not in terminals:
                    [r] = r
                    terminals.append(r)
                R[left].append([r])
            else:
                R[left].append(r)

    return non_terminals, terminals, R

def main():
    path = "./CNF.txt"
    non_terminals, terminals, R = readCNF(path)
    print("non_terminals =", non_terminals)
    print("terminals =", terminals)
    print("R =", R)

if __name__ == "__main__":
    main()
