#Kunal Gautam
#Codewars : @Kunalpod
#Problem name: Find Multiples of a Number
#Problem level: 8 kyu

def find_multiples(integer, limit):
    return [integer*i for i in range(1,limit//integer+1)]
