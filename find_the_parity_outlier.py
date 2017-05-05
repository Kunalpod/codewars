#Kunal Gautam
#Codewars : @Kunalpod
#Problem name: Find The Parity Outlier
#Problem level: 6 kyu

def find_outlier(integers):
    x1 = filter(lambda x: x%2==0, integers)
    x2 = filter(lambda x: x%2==1, integers)
    if len(x1) == 1:
        return x1[0]
    return x2[0] 
