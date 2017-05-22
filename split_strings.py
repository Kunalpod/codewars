#Kunal Gautam
#Codewars : @Kunalpod
#Problem name: Split Strings
#Problem level: 6 kyu

def solution(s):
    return [s[i:i+2] for i in range(0, len(s), 2)][:-1] + [s[-1:]+'_'] if len(s)%2 else [s[i:i+2] for i in range(0, len(s), 2)]
