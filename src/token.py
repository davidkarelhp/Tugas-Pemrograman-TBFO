import re

def tokenizeInput(inputFilename):
    # Read from file
    f = open(inputFilename, "r", encoding='utf8')
    contents = f.read()
    contents = contents.split()
    f.close()

    result = contents

    operators = [':', ',', '=', '<', '>', '>=', '<=', '==', '!=', r'\+', '-', r'\*', '/', r'\*\*', r'\(', r'\)' , r'\[' , r'\]',r'\'\'\'', r'\"\"\"']

    # For each operator..
    for operator in operators:
        temporaryResult = []
        # For each statement..
        for statement in result:
            format = r"[A..z]*(" + operator +r")[A..z]*"
            x = re.split(format, statement)
            
            # Append 
            for splitStatement in x:
                temporaryResult.append(splitStatement) 
        result = temporaryResult

    # check three quote
    temporaryResult = []
    for res in result:
        if (res == "'''"):
            temporaryResult.append("threeOneQuote")
        elif (res == '"""'):
            temporaryResult.append("threeTwoQuote")
        else:
            temporaryResult.append(res)
    result = temporaryResult

    operators = [r'\'', r'\"']
    # check one quote
    for operator in operators:
        temporaryResult = []
        # For each statement..
        for statement in result:
            format = r"[A..z]*(" + operator +r")[A..z]*"
            x = re.split(format, statement)
            
            # Append 
            for splitStatement in x:
                temporaryResult.append(splitStatement) 
        result = temporaryResult
    # Strip space
    temporaryResult = []
    for statement in result:
        stripped = statement.split()
        for splitStatement in stripped: 
            temporaryResult.append(splitStatement)

    result = temporaryResult

    # Strip empty string
    result = [string for string in result if string!='']

    # Strip comment
    temporaryResult = []
    comment = False
    quote = ""
    for res in result:
        if (res == "'" or res == '"' or res == "threeOneQuote" or res == "threeTwoQuote"):
            if (comment):
                if (res == quote):
                    comment = False
            else:
                quote = res 
                comment = True
                if (quote == 'threeOneQuote'):
                    temporaryResult.append("'")
                    temporaryResult.append("'")
                    temporaryResult.append("'")
                elif (quote == 'threeTwoQuote'):
                    temporaryResult.append('"')
                    temporaryResult.append('"')
                    temporaryResult.append('"')
                else:
                    temporaryResult.append(quote)
        if (not comment):
            if (quote == 'threeOneQuote'):
                temporaryResult.append("'")
                temporaryResult.append("'")
                temporaryResult.append("'")
                quote = ""
            elif (quote == 'threeTwoQuote'):
                temporaryResult.append('"')
                temporaryResult.append('"')
                temporaryResult.append('"')
                quote = ""
            else:
                temporaryResult.append(res)
        else:
            temporaryResult.append('comment')
    result = temporaryResult

    for i in range(len(result) - 1):
        if (i >= len(result) - 1):
            break
        if (result[i] == '<' or result[i] == '>' or result[i] == '=' or result[i] == '!'):
            if (result[i + 1] == '='):
                result[i] = result[i] + result[i + 1]
                del result[i + 1]

    for i in range(len(result) - 1):
        if (i >= len(result) - 1):
            break
        if (result[i] == '*'):
            if (result[i + 1] == '*'):
                result[i] = result[i] + result[i + 1]
                del result[i + 1]
    
    for i in range(len(result) - 1):
        if (i >= len(result) - 1):
            break
        if (result[i] == '/'):
            if (result[i + 1] == '/'):
                result[i] = result[i] + result[i + 1]
                del result[i + 1]

    return result