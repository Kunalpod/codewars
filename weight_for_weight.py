#Kunal Gautam
#Codewars : @Kunalpod
#Problem name: Weight for weight
#Problem level: 5 kyu

from itertools import groupby
def order_weight(strng):
    li = sorted([x for x in strng.split()], key=lambda y: sum([int(x) for x in y]))
    l = [sorted(list(grp)) for _, grp in groupby(li, lambda y: sum([int(x) for x in y]))]
    return ' '.join([item for sublist in l for item in sublist])
