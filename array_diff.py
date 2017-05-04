#Kunal Gautam
#Codewars : @Kunalpod
#Problem name: Array.diff
#Problem level: 6 kyu

def array_diff(a, b):
    for ele in b:
        while ele in a:
            a.pop(a.index(ele))
    return a  
