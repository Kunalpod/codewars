#Kunal Gautam
#Codewars : @Kunalpod
#Problem name: Common Denominators
#Problem level: 5 kyu

from fractions import gcd
def convertFracts(lst):
    den = [y for x,y in lst]
    g = 1
    while(den):
        x = den.pop()
        g = (g*x) // gcd(g,x)
    return [[x*g//y, g] for x,y in lst]
