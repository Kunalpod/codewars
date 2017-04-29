#Kunal Gautam
#Codewars : @Kunalpod
#Problem name: Simple Fun #4: Phone Call
#Problem level: 7 kyu

def phone_call(min1, min2_10, min11, s):
    if s<min1:    return 0
    if s==min1:    return 1
    else:
        t = 1
        s -=min1
        if s<=min2_10*9:
            t += s//min2_10
            s -= (s//min2_10)*min2_10
        else:
            t += 9
            s -= min2_10*9
            t += s//min11
    return t        
