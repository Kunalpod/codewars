#Kunal Gautam
#Codewars : @Kunalpod
#Problem name: Complete The Pattern #4
#Problem level: 7 kyu

def pattern(n):
    return '\n'.join((''.join(str(j) for j in range(i, n+1))) for i in range(1, n+1))
