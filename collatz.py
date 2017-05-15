#Kunal Gautam
#Codewars : @Kunalpod
#Problem name: Collatz
#Problem level: 6 kyu

def collatz(n):
    li = [n]
    while(n!=1):
        n = n//2 if not n%2 else 3*n + 1
        li.append(n)
    return '->'.join(str(x) for x in li)    
