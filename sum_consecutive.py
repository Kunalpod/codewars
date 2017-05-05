#Kunal Gautam
#Codewars : @Kunalpod
#Problem name: Sum consecutives
#Problem level: 6 kyu

from itertools import groupby
def sum_consecutives(s):
    return [sum(list(group)) for _,group in groupby(s)]
