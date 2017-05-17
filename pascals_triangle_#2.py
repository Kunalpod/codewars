#Kunal Gautam
#Codewars : @Kunalpod
#Problem name: Pascal's triangle #2
#Problem level: 5 kyu

def pascal(p):
    li=[[1], [1, 1]]
    for i in range(2, p):
        t = [1] + [li[i-1][j]+li[i-1][j+1] for j in range(i-1)] + [1]
        li.append(t)
    return li[:p]
