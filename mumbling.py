#Kunal Gautam
#Codewars : @Kunalpod
#Problem name: Mumbling
#Problem level: 7 kyu

def accum(s):
    li = []
    for i in range(len(s)):
        li.append(s[i].upper() + s[i].lower()*i)
    return '-'.join(li)
