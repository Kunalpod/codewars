#Kunal Gautam
#Codewars : @Kunalpod
#Problem name: Arabian String
#Problem level: 6 kyu

import re
def camelize(str_):
    return ''.join([x[0].upper()+x[1:].lower() for x in re.split('[^0-9A-Za-z]*', str_) if x])
