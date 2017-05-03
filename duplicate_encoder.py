#Kunal Gautam
#Codewars : @Kunalpod
#Problem name: Duplicate Encoder
#Problem level: 6 kyu

def duplicate_encode(word. st=""):
    for char in word.lower():
        if word.lower().count(char)>1:    st = st + ')'
        else:    st = st + '('
    return st
