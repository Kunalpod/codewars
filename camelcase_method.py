#Kunal Gautam
#Codewars : @Kunalpod
#Problem name: CamelCase Method
#Problem level: 6 kyu

def camel_case(string):    return ''.join([x[0].upper()+x[1:] for x in string.lower().split()])
