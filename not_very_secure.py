#Kunal Gautam
#Codewars : @Kunalpod
#Problem name: Not very secure
#Problem level: 5 kyu

import re
def alphanumeric(string):    
    return bool(re.findall('[a-zA-Z0-9]+', string)) and re.findall('[a-zA-Z0-9]+', string)[0] == string
