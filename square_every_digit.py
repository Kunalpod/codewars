#Kunal Gautam
#Codewars : @Kunalpod
#Problem name: Square Every Digit
#Problem level: 7 kyu

def square_digits(num):
    return int(''.join([str(int(x)**2) for x in str(num)]))
