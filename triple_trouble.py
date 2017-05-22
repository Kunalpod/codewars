#Kunal Gautam
#Codewars : @Kunalpod
#Problem name: Triple trouble
#Problem level: 6 kyu

def triple_double(num1, num2):
    for i in range(10):
        if str(i)*3 in str(num1) and str(i)*2 in str(num2):
            return 1
    return 0
