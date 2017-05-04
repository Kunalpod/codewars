#Kunal Gautam
#Codewars : @Kunalpod
#Problem name: Is a number prime?
#Problem level: 6 kyu

from math import sqrt
def is_prime(num):
    if num==0 or abs(num)==1:
        return False
    for i in range(2,int(sqrt(num))+1):
        if num%i==0:
            return False
    return True   
