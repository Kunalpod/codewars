#Kunal Gautam
#Codewars : @Kunalpod
#Problem name: Two to One
#Problem level: 7 kyu

from itertools import groupby
def longest(s1, s2):
    return ''.join([key for key,_ in groupby(sorted(list(s1+s2)))])
