#Kunal Gautam
#Codewars : @Kunalpod
#Problem name: Simple Fun #204: Smallest Integer
#Problem level: 7 kyu

from itertools import groupby, chain
def smallest_integer(matrix):
    min = pos = 0
    for key,_ in groupby([x for x in sorted(list(chain.from_iterable(matrix))) if x>=0]): 
        if key==min:
            min+=1
            pos+=1
        else:
            return min
    return min
