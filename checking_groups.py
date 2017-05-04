#Kunal Gautam
#Codewars : @Kunalpod
#Problem name: Checking Groups
#Problem level: 6 kyu

def group_check(s):
    li=[]
    print(s)
    for symb in s:
        if symb=='(' or symb=='[' or symb=='{':
            li.append(symb)
        else:
            if li:
                x=li.pop()
                if (x=='(' and symb==')') or (x=='{' and symb=='}') or (x=='[' and symb==']'):
                    pass
                    print("H")
                else:    
                    return False
            else:    return False        
    if li:    
        return False
    return True
