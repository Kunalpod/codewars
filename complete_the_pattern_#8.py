#Kunal Gautam
#Codewars : @Kunalpod
#Problem name: Complete The Pattern #8 - Number Pyramid
#Problem level: 6 kyu

def pattern(n):
    return '\n'.join(' '*(n-i) + ''.join(str(j%10) for j in range(1, i+1)) + ''.join(str(j%10) for j in list(range(1,i))[::-1]) + ' '*(n-i) for i in range(1, n+1))
