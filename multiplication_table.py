#Kunal Gautam
#Codewars : @Kunalpod
#Problem name: Multiplication Table
#Problem level: 6 kyu

def multiplication_table(row,col):
    return [[x*y for y in range(1,col+1)] for x in range(1,row+1)]
