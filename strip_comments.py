#Kunal Gautam
#Codewars : @Kunalpod
#Problem name: Strip Comments
#Problem level: 4 kyu

def solution(string,markers):
    li=string.split("\n")
    for i in range(len(li)):
        for symb in markers:    
            if symb in li[i]:
                li[i]=li[i].split(symb)[0]
        li[i] = li[i].rstrip()   
    return '\n'.join(li)                
