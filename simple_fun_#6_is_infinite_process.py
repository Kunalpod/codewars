#Kunal Gautam
#Codewars : @Kunalpod
#Problem name: Simple Fun #6: Is Infinite Process?
#Problem level: 7 kyu

def is_infinite_process(a, b):
    if b<a:    return True
    if (b-a)%2==1:    return True
    return False
