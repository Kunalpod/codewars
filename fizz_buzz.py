#Kunal Gautam
#Codewars : @Kunalpod
#Problem name: Fizz/Buzz
#Problem level: 6 kyu

def solution(number):
    s3 = s5 = s35 =0
    for x in range(1, number):
        if not x%3: s3+=1
        if not x%5: s5+=1
        if not x%15: s35+=1
    return [s3-s35, s5-s35, s35]
