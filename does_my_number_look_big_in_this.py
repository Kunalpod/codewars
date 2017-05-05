#Kunal Gautam
#Codewars : @Kunalpod
#Problem name: Does my number look big in this?
#Problem level: 6 kyu

def narcissistic( value ):
    return value==int(sum([int(x)**len(str(value)) for x in str(value)]))
