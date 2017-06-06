#Kunal Gautam
#Codewars : @Kunalpod
#Problem name: Least Common Multiple
#Problem level: 5 kyu

from fractions import gcd
def lcm(*args):
    l = args[0]
    for a in args[1:]:    l = l * a // gcd(l,a)
    return l
