#Kunal Gautam
#Codewars : @Kunalpod
#Problem name: String Incrementer
#Problem level: 5 kyu

import re
def increment_string(strng):
    if not strng or strng[-1] not in "0123456789":    return strng + "1"
    num = [x for x in re.findall('[0-9]*', strng) if x]
    return strng.replace(num[-1], ('{:0>'+str(len(num[-1]))+'}').format(int(num[-1])+1))
