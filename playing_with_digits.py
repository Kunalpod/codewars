#Kunal Gautam
#Codewars : @Kunalpod
#Problem name: Playing with digits
#Problem level: 6 kyu

def dig_pow(n, p):
    s = 0
    for i in range(len(str(n))):
        s += int(str(n)[i])**(i+p)
    return s//n if s%n==0 else -1
