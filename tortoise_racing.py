#Kunal Gautam
#Codewars : @Kunalpod
#Problem name: Tortoise racing
#Problem level: 6 kyu

def race(v1, v2, g):
    if v1>=v2: return None
    sec = g*3600/(v2-v1)    
    return [sec//3600, int(sec%3600)//60, int(sec%3600%60)]
