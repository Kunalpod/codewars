#Kunal Gautam
#Codewars : @Kunalpod
#Problem name: Is this a triangle?
#Problem level: 7 kyu

def is_triangle(a, b, c):
    return (a+b>c) and (b+c>a) and (c+a>b)
