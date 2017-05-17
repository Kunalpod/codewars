#Kunal Gautam
#Codewars : @Kunalpod
#Problem name: Convert PascalCase string into snake_case
#Problem level: 5 kyu

import re
def to_underscore(string):
    string = str(string)
    if not re.findall('[A-Z]', string):    return str(string)
    return '_'.join(re.findall('[A-Z][a-z0-9]*', string)).lower()
