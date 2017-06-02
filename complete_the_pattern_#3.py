#Kunal Gautam
#Codewars : @Kunalpod
#Problem name: Complete The Pattern #3 (Horizontal Image of #2)
#Problem level: 7 kyu

def pattern(n):
    return '\n'.join(''.join(str(i) for i in reversed(list(range(x, n+1)))) for x in list(range(1, n+1))[::-1])
