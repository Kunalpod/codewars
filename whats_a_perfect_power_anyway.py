#Kunal Gautam
#Codewars : @Kunalpod
#Problem name: What's a Perfect Power anyway?
#Problem level: 5 kyu

def isPP(n):
    for i in range(2, int(n**0.5) + 1):
        if not n%i:
            po = 2
            while(1):
                if i**po == n:    return [i, po]
                elif i**po > n: break
                po += 1
    return None
