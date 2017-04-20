#Kunal Gautam
#Codewars : @Kunalpod
#Problem name: Scramblies
#Problem level: 5 kyu

from itertools import groupby
def scramble(s1,s2):
    for key, group in groupby(sorted(s2)):
        if len(list(group)) > s1.count(key):
            return False
    return True        
