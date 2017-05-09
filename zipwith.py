#Kunal Gautam
#Codewars : @Kunalpod
#Problem name: zipWith
#Problem level: 6 kyu

def zip_with(fn,a1,a2):
    return [fn(a1[i],a2[i]) for i in range(min(len(a1),len(a2)))]
