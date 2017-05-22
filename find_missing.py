#Kunal Gautam
#Codewars : @Kunalpod
#Problem name: Find the missing term in an Arithmetic Progression
#Problem level: 5 kyu

def find_missing(s):
    for i in range(1, len(s)-1):
        if s[i]-s[i-1] != s[i+1]-s[i]:
            return 2*s[i]-s[i-1] if abs(s[i] - s[i-1]) < abs(s[i+1] - s[i]) else 2*s[i]-s[i+1]
