#Kunal Gautam
#Codewars : @Kunalpod
#Problem name: Trumpness Detector
#Problem level: 6 kyu

import re
from itertools import groupby
def trump_detector(trump_speech):
    count1 = 0
    count2 = 0
    for chr in re.findall('[aeiou]+', trump_speech.lower()):
        count1 += sum(len(list(grp))-1 for k, grp in groupby(sorted(chr)))
        count2 += sum(1 for k, grp in groupby(chr))
    return round(count1 / count2, 2) if count1 else 0
