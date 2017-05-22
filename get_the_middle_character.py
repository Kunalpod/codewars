#Kunal Gautam
#Codewars : @Kunalpod
#Problem name: Get the Middle Character
#Problem level: 7 kyu

def get_middle(s):
    return s[len(s) // 2 - 1 : len(s) // 2 + 1] if not len(s)%2 else s[len(s)//2]
