#Kunal Gautam
#Codewars : @Kunalpod
#Problem name: Complete The Pattern #2
#Problem level: 7 kyu

def pattern(n):
    return '\n'.join(''.join(str(i) for i in reversed(list(range(x, n+1)))) for x in range(1, n+1))
