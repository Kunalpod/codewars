#Kunal Gautam
#Codewars : @Kunalpod
#Problem name: Find Factors Down to Limit
#Problem level: 8 kyu

def factors(integer, limit):
    return [x for x in range(limit,(integer//2)+1) if not integer%x] + ([integer] if integer>=limit else []) 
