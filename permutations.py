#Kunal Gautam
#Codewars : @Kunalpod
#Problem name: Permutations
#Problem level: 4 kyu

from itertools import groupby, permutations as perm
def permutations(string):
    return [k for k,_ in groupby(sorted([''.join(comb) for comb in perm(string)]))]
