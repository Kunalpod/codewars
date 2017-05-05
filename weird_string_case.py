#Kunal Gautam
#Codewars : @Kunalpod
#Problem name: WeIrD StRiNg CaSe
#Problem level: 6 kyu

def funk(str):
    for i in range(len(str)):
        if not i%2:    str[i]=str[i].upper()
    return ''.join(str)    
def to_weird_case(string):
    return ' '.join([funk(list(x)) for x in string.lower().split()])
