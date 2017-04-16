#Kunal Gautam
#Codewars : @Kunalpod
#Problem name: Counting Duplicates
#Problem level: 6 kyu

from itertools import groupby
def duplicate_count(text):
    count = 0
    for key, group in groupby(sorted(text.lower())):
        if len(list(group))>1:
            count += 1
    return count
