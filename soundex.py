#Kunal Gautam
#Codewars : @Kunalpod
#Problem name: Soundex
#Problem level: 5 kyu

import re
from itertools import groupby
vowel = ['a', 'e', 'i', 'o', 'u', 'y']
def codeit(word):
    letter = word[0].lower()
    arr = ''.join([letter] + [x for x in word.lower()[1:] if x!='h' and x!='w'])
    arr = re.sub('[bfpv]', '1', arr)
    arr = re.sub('[cgjkqsxz]', '2', arr)
    arr = re.sub('[dt]', '3', arr)
    arr = re.sub('[l]', '4', arr)
    arr = re.sub('[mn]', '5', arr)
    arr = re.sub('[r]', '6', arr)
    arr = [k for k,_ in groupby(arr)]
    arr = [x for x in arr[1:] if x not in vowel][:3]
    return '{:<04}'.format(letter + ''.join(arr)).upper()

def soundex(name):
    return ' '.join([codeit(word) for word in name.split()])
