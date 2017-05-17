#Kunal Gautam
#Codewars : @Kunalpod
#Problem name: Reverse polish notation calculator
#Problem level: 4 kyu

def calc(expr):
    li = [0]
    for char in expr.split():
        try: li.append(float(char))
        except: 
            x = li.pop()
            li.append(eval('li.pop()'+char+'x'))
    return li.pop()
