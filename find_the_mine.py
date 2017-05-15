#Kunal Gautam
#Codewars : @Kunalpod
#Problem name: Find the Mine!
#Problem level: 6 kyu

def mineLocation(field):
    for i in range(len(field)):
        for j in range(len(field)):
            if field[i][j]==1:    return [i,j]
