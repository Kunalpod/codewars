#Kunal Gautam
#Codewars : @Kunalpod
#Problem name: Complete The Pattern #16
#Problem level: 6 kyu

def pattern(n):
    return '\n'.join(''.join(str(j%10) for j in list(range(n-i+1, n+1))[::-1]) + ''.join(str((n-i+1)%10) for j in range(n-i)) for i in range(1, n+1))
