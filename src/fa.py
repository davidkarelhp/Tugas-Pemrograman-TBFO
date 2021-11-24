OP = ['+', '-', '/', '%', '*', '**']
NA = ['pass', 'break', 'continue']
BN = ['True', 'False', 'None']
def VV(str):
    return str.isidentifier()
COMP = ['==', '<=', '>=', '!=', '<', '<']
def NUM(str):
    return str.isnumeric()
ASS = ['=']
FINALSTATES = ['S', 'A', 'B', 'C', 'D']
def fa(array):
    current_state = 'S'
    n = len(array)
    # print(array)
    # print("start")
    for i in range(n):
        # print("state " + current_state)
        # print(array[i])
        if (current_state == 'S'):
            if (array[i] in OP or array[i] in COMP or array[i] in ASS):
                return False
            elif (NUM(array[i])):
                current_state = 'A'
            elif (array[i] in NA):
                current_state = 'C'
            elif (array[i] in BN):
                current_state = 'D'
            elif (VV(array[i])):
                current_state = 'B'
            else:
                return False
        elif (current_state == 'A'):
            if (array[i] in OP or array[i] in ASS):
                return False
            elif (NUM(array[i])):
                current_state = 'A'
            elif (array[i] in NA):
                current_state = 'C'
            elif (array[i] in BN):
                current_state = 'D'
            elif (array[i] in COMP):
                current_state = 'E'
            elif (VV(array[i])):
                current_state = 'B'
            else:
                return False
        elif (current_state == 'B'):
            if (array[i] in OP or array[i] in COMP or array[i] in ASS):
                current_state = 'E'
            elif (NUM(array[i])):
                current_state = 'A'
            elif (array[i] in NA):
                current_state = 'C'
            elif (array[i] in BN):
                current_state = 'D'
            elif (VV(array[i])):
                current_state = 'B'
            else:
                return False
        elif (current_state == 'C'):
            if (array[i] in OP or array[i] in COMP or array[i] in ASS):
                return False
            elif (NUM(array[i])):
                current_state = 'A'
            elif (array[i] in NA):
                current_state = 'C'
            elif (array[i] in BN):
                current_state = 'D'
            elif (VV(array[i])):
                current_state = 'B'
            else:
                return False
        elif (current_state == 'D'):
            if (array[i] in ASS):
                return False
            elif (NUM(array[i])):
                current_state = 'A'
            elif (array[i] in NA):
                current_state = 'C'
            elif (array[i] in BN):
                current_state = 'D'
            elif (array[i] in OP or array[i] in COMP):
                current_state = 'E'
            elif (VV(array[i])):
                current_state = 'B'
            else:
                return False
        elif (current_state == 'E'):
            if (array[i] in OP or array[i] in COMP or array[i] in ASS):
                return False
            elif (NUM(array[i])):
                current_state = 'A'
            elif (array[i] in NA):
                current_state = 'C'
            elif (array[i] in BN):
                current_state = 'D'
            elif (VV(array[i])):
                current_state = 'B'
            else:
                return False
    # print('state')
    # print("endstate " + current_state)
    return current_state in FINALSTATES






