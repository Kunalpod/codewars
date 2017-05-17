#Kunal Gautam
#Codewars : @Kunalpod
#Problem name: Pete, the baker
#Problem level: 5 kyu

def cakes(recipe, available):
    for item in recipe:    
        if item not in available:    return 0
    return min([available[x]//recipe[x] for x in recipe])
