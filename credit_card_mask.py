#Kunal Gautam
#Codewars : @Kunalpod
#Problem name: Credit Card Mask
#Problem level: 7 kyu

def maskify(cc):
    if len(cc)>=4:
         return ''.join(["#" for _ in cc[:-4]])+cc[-4:]
    return cc
