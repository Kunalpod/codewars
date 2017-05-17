#Kunal Gautam
#Codewars : @Kunalpod
#Problem name: Valid Braces
#Problem level: 4 kyu

valid = {'(': ')', '[': ']', '{': '}'}
def validBraces(string):
    li=[]
    for item in string:
        if item in valid:    li.append(item)
        elif li and valid[li[-1]] == item:    li.pop()
        else:    return False
    return False if li else True
