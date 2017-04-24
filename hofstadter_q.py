#Kunal Gautam
#Codewars : @Kunalpod
#Problem name: Hofstadter Q
#Problem level: 6 kyu

def load(n):
    hof=[0, 1, 1]
    for i in range(3,n+1):
        hof.append(hof[i - hof[i-1]] + hof[i - hof[i-2]])
    return hof    
          
def hofstadter_Q(n):
    hof = load(n)
    return hof[n]
