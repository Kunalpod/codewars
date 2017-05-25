#Kunal Gautam
#Codewars : @Kunalpod
#Problem name: Simple Fun #258: Is Divisible By 6
#Problem level: 6 kyu

def is_divisible_by_6(s):
    return [str(int(s.split('*')[0] + str(x) + s.split('*')[1])) for x in range(10) if int(s.split('*')[0] + str(x) + s.split('*')[1]) and not int(s.split('*')[0] + str(x) + s.split('*')[1])%6]
