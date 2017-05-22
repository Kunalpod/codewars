#Kunal Gautam
#Codewars : @Kunalpod
#Problem name: Spelling Bee
#Problem level: 6 kyu

def how_many_bees(hive):
    if not hive: return 0
    count = 0
    for i in range(len(hive)):
        for j in range(len(hive[i])):
            try:    
                if hive[i][j]=='b' and hive[i][j+1]=='e' and hive[i][j+2]=='e': count += 1                    
            except:    pass
            try:    
                if j-2>=0 and hive[i][j]=='b' and hive[i][j-1]=='e' and hive[i][j-2]=='e': count += 1                    
            except:    pass
            try:    
                if hive[i][j]=='b' and hive[i+1][j]=='e' and hive[i+2][j]=='e': count += 1                    
            except:    pass
            try:    
                if i-2>=0 and hive[i][j]=='b' and hive[i-1][j]=='e' and hive[i-2][j]=='e': count += 1
            except:    pass
    return count
