#Kunal Gautam
#Codewars : @Kunalpod
#Problem name: Which are in?
#Problem level: 6 kyu

from itertools import groupby
def in_array(array1, array2):
    return [key for key,_ in groupby(sorted([x for x in array1 for y in array2 if x in y]))]
