#Kunal Gautam
#Codewars : @Kunalpod
#Problem name: Word a10n (abbreviation)
#Problem level: 6 kyu

import re
def abbreviate(s):
    words = re.findall('[A-Za-z][A-Za-z][A-Za-z][A-Za-z]+', s)
    for word in words:
        s = s.replace(word, word[0] + str(len(word) - 2) + word[-1])
    return s
