#Kunal Gautam
#Codewars : @Kunalpod
#Problem name: You're a square
#Problem level: 7 kyu

def is_square(n):    
    if n<=0: return False
    return (n**0.5).is_integer()
