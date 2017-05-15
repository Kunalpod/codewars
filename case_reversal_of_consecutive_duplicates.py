#Kunal Gautam
#Codewars : @Kunalpod
#Problem name: Case Reversal of Consecutive Duplicates
#Problem level: 6 kyu

from itertools import groupby
def reverse(str):
    s = ''
    for key, grp in groupby(str):
        l = len(list(grp))
        if l>1:
            if key.isupper():
                s += (key*l).lower()
            else:
                s += (key*l).upper()    
        else: s += key
    return s
