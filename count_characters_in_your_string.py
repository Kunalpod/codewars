#Kunal Gautam
#Codewars : @Kunalpod
#Problem name: Count characters in your string
#Problem level: 6 kyu

from itertools import groupby
def count(string):
    dict = {}
    for key,grp in groupby(sorted(string)):
        dict[key] = len(list(grp))
    return dict
