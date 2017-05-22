#Kunal Gautam
#Codewars : @Kunalpod
#Problem name: Largest 5 digit number in a series
#Problem level: 5 kyu

def solution(digits):
    return max(int(digits[i:i+5]) for i in range(len(digits)-4))
