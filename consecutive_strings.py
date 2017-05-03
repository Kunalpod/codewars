#Kunal Gautam
#Codewars : @Kunalpod
#Problem name: Consecutive Strings
#Problem level: 6 kyu

def longest_consec(strarr, k):
    if len(strarr)==0 or len(strarr)<k or k<=0:    return ""
    max = len(''.join(strarr[0:k]))
    index = 0
    for i in range(1,len(strarr)-k+1):
        if len(''.join(strarr[i:i+k]))>max:
            max=len(''.join(strarr[i:i+k]))
            index=i
    return ''.join(strarr[index:index+k])
