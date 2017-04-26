#Kunal Gautam
#Codewars : @Kunalpod
#Problem name: Heads and Legs
#Problem level: 8 kyu

def animals(heads, legs):
    if heads==0 and legs==0:
        return (0,0)
    y = legs//2 - heads
    x = heads-y
    if x<0 or y<0 or legs%2!=0:
        return "No solutions"
    return (x,y)
