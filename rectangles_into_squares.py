#Kunal Gautam
#Codewars : @Kunalpod
#Problem name: Rectangles into Squares
#Problem level: 6 kyu

def sqInRect(lng, wdth):
    if lng==wdth: return None
    li=[]
    while lng and wdth:
        if lng>wdth:
            lng-=wdth
            li.append(wdth)
        else:
            wdth-=lng
            li.append(lng)
    return li
