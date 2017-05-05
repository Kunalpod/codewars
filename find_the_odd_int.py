#Kunal Gautam
#Codewars : @Kunalpod
#Problem name: Find the odd int
#Problem level: 6 kyu

from itertools import groupby
def find_it(seq):
    for key, group in groupby(sorted(seq), lambda x: x):
        if(len(list(group))%2==1):
            return key
