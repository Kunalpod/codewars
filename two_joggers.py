#Kunal Gautam
#Codewars : @Kunalpod
#Problem name: Two Joggers
#Problem level: 5 kyu

from fractions import gcd
def nbr_of_laps(x, y):
    return [x*y//gcd(x,y)//x, x*y//gcd(x,y)//y]
