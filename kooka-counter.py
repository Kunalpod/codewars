#Kunal Gautam
#Codewars : @Kunalpod
#Problem name: Kooka-Counter
#Problem level: 7 kyu

from itertools import groupby
def kooka_counter(laughing):
    return len([key for key,_ in groupby(laughing.split('a')[:-1])])
