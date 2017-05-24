#Kunal Gautam
#Codewars : @Kunalpod
#Problem name: Strings Mix
#Problem level: 4 kyu

from itertools import groupby
def mix(s1, s2):
    s1 = {key:len(list(grp)) for key, grp in groupby(sorted([x for x in s1 if x.islower()]))}
    s2 = {key:len(list(grp)) for key, grp in groupby(sorted([x for x in s2 if x.islower()]))}
    li = []
    for key in s1:
        if key in s2:
            if s1[key] == 1 and s2[key] == 1:    continue
            if s1[key] > s2[key]:    li.append('1:'+key*s1[key])
            elif s1[key] < s2[key]:    li.append('2:'+key*s2[key])
            else:    li.append('=:'+key*s2[key])
        else:    
            if s1[key] !=1:    li.append('1:'+key*s1[key])
    for key in s2:
        if key not in s1 and s2[key] != 1:    li.append('2:'+key*s2[key])
    return '/'.join(sorted(sorted(li), key = lambda x: len(x)*-1))
