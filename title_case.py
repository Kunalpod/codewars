#Kunal Gautam
#Codewars : @Kunalpod
#Problem name: Title Case
#Problem level: 6 kyu

def title_case(title, minor_words=''):
    if not title: return ''
    li = title.lower().split()
    li[0] = li[0][0].upper()+li[0][1:]
    for i in range(1, len(li)):
        if li[i] not in minor_words.lower().split():
            li[i] = li[i][0].upper()+li[i][1:]
    return ' '.join(li)
