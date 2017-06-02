#Kunal Gautam
#Codewars : @Kunalpod
#Problem name: Complete The Pattern #6 - Odd Ladder
#Problem level: 7 kyu

def pattern(n):
    return "\n".join(str(i)*i for i in range(1, n+1) if i%2)
