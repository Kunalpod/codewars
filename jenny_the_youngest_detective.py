#Kunal Gautam
#Codewars : @Kunalpod
#Problem name: Jenny the youngest detective
#Problem level: 7 kyu

def missing(nums, ss):
    ss = ''.join(ss.split()).lower()
    return ''.join([ss[i] for i in sorted(nums)]) if max(nums) < len(ss) else "No mission today"
