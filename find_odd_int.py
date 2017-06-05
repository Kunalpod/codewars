#Kunal Gautam
#Codewars : @Kunalpod
#Problem name: Find the odd int
#Problem level: 6 kyu

from itertools import groupby
def find_it(seq):
    return [key for key, group in groupby(sorted(seq)) if len(list(group))%2][0]
