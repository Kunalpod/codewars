#Kunal Gautam
#Codewars : @Kunalpod
#Problem name: Jaden Casing Strings
#Problem level: 7 kyu

def toJadenCase(string):
    return " ".join(x[0].upper()+x[1:] for x in string.split())
