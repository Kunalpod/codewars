#Kunal Gautam
#Codewars : @Kunalpod
#Problem name: IP Validation
#Problem level: 4 kyu

import re
def is_valid_IP(strng):
    li = strng.split('.')
    if len(li)!=4: return False
    for i in li:
        if not len(i): return False
        if re.match('[a-zA-Z]+',i): return False
        if not (int(i)<=255 and int(i)>=0 and i==str(int(i))):
            return False
    return True    
