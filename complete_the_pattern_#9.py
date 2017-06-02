#Kunal Gautam
#Codewars : @Kunalpod
#Problem name: Complete The Pattern #9 - Diamond
#Problem level: 6 kyu

def pattern(n):
    top = '\n'.join(' '*(n-i) + ''.join(str(j%10) for j in range(1, i+1)) + ''.join(str(j%10) for j in list(range(1,i))[::-1]) + ' '*(n-i) for i in range(1, n+1))
    bottom = '\n'.join(' '*(n-i) + ''.join(str(j%10) for j in range(1, i+1)) + ''.join(str(j%10) for j in list(range(1,i))[::-1]) + ' '*(n-i) for i in list(range(1, n))[::-1])
    return top + '\n' + bottom if bottom else top
