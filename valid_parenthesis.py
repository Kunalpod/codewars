#Kunal Gautam
#Codewars : @Kunalpod
#Problem name: Valid Parentheses
#Problem level: 5 kyu

def valid_parentheses(string):
    counter = 0
    for ch in string:
        if ch=='(' or ch==')':
            if ch == '(':    counter += 1
            elif ch == ')' and counter != 0: counter -= 1
            else:    return False
    return True if counter==0 else False
