#Kunal Gautam
#Codewars : @Kunalpod
#Problem name: Next bigger number with the same digits
#Problem level: 4 kyu

from itertools import permutations, groupby
def next_bigger(n):
    if int(''.join(sorted(str(n), reverse = True))) == n:    return -1
    for i in reversed(range(0,len(str(n))-1)):
        ss = [k for k,_ in groupby(sorted([int(str(n)[:i] + ''.join(comb)) for comb in permutations(str(n)[i:])]))]
        if n==ss[-1]:    continue
        else:    return ss[ss.index(n) + 1]
