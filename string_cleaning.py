#Kunal Gautam
#Codewars : @Kunalpod
#Problem name: String cleaning
#Problem level: 8 kyu

def string_clean(s):
    return ''.join([x for x in s if not x.isdigit()])
