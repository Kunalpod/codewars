#Kunal Gautam
#Codewars : @Kunalpod
#Problem name: Count the smiley faces!
#Problem level: 6 kyu

import re
def count_smileys(arr):
    return sum([1 for x in arr if bool(re.match('[;:][-~]*[)D]',x))])
