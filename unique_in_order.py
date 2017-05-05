#Kunal Gautam
#Codewars : @Kunalpod
#Problem name: Unique In Order
#Problem level: 6 kyu

from itertools import groupby
def unique_in_order(iterable):
    return [key for key,_ in groupby(iterable)]
