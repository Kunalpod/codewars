#Kunal Gautam
#Codewars : @Kunalpod
#Problem name: Complete The Pattern #11 - Plus
#Problem level: 6 kyu

def pattern(n):
    if n < 1: return ""
    top = '\n'.join(' '*(n-1) + str(i%10)*n + ' '*(n-1) for i in range(1,n))
    middle = '\n'.join(''.join(str(j%10) for j in range(1,n)) + str(n%10)*n + ''.join(str(j%10) for j in list(range(1,n))[::-1]) for i in range(1,n+1))
    bottom = '\n'.join(' '*(n-1) + str(i%10)*n + ' '*(n-1) for i in list(range(1,n))[::-1])
    return '\n'.join([top, middle, bottom])
