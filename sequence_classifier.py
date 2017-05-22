#Kunal Gautam
#Codewars : @Kunalpod
#Problem name: Sequence classifier
#Problem level: 7 kyu

from itertools import groupby
def sequence_classifier(arr):
    if len([k for k,_ in groupby(arr)]) == 1: return 5
    elif sorted(arr) == arr:
        if len([k for k,_ in groupby(arr)]) != len(arr): return 2
        return 1
    elif sorted(arr, reverse=True) == arr:
        if len([k for k,_ in groupby(arr)]) != len(arr): return 4
        return 3
    return 0
