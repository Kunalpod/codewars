#Kunal Gautam
#Codewars : @Kunalpod
#Problem name: Sorting Arrays by the Amount of Perfect Squares that Each Element May Generate
#Problem level: 5 kyu

from itertools import permutations, groupby
def sort_by_perfsq(arr):    return sorted(sorted(arr), key = lambda x: len([key for key,_ in groupby(sorted([''.join(comb) for comb in permutations(str(x)) if int(''.join(comb))**0.5 == int(int(''.join(comb))**0.5)]))]), reverse = True)
