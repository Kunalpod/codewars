#Kunal Gautam
#Codewars : @Kunalpod
#Problem name: Simple Fun #262: Case Unification
#Problem level: 7 kyu

import re
def case_unification(ss):
    return ss.lower() if len(re.findall('[a-z]', ss)) > len(ss)/2 else ss.upper()
