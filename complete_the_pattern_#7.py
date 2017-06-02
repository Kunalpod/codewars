#Kunal Gautam
#Codewars : @Kunalpod
#Problem name: Complete The Pattern #7
#Problem level: 7 kyu

def pattern(n):
    return '\n'.join(''.join(str(j) for j in range(i, n+1)) + ''.join(str(j) for j in range(1, i)) for i in range(1,n+1))
