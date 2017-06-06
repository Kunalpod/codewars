#Kunal Gautam
#Codewars : @Kunalpod
#Problem name: Detect Panagram
#Problem level: 6 kyu

from itertools import groupby
a = "abcdefghijklmnopqrstuvwxyz"
def is_pangram(s):
    return a in ''.join(key for key,_ in groupby(sorted(s.lower())))
