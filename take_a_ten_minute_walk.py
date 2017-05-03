#Kunal Gautam
#Codewars : @Kunalpod
#Problem name: Take a Ten Minute Walk
#Problem level: 6 kyu

def isValidWalk(walk):
    return walk.count('n')==walk.count('s') and walk.count('e')==walk.count('w')
