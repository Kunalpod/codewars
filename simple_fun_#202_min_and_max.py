#Kunal Gautam
#Codewars : @Kunalpod
#Problem name: Simple Fun #202: Min And Max
#Problem level: 7 kyu

def min_and_max(l, d, num):
  li = [x for x in range(l,d+1) if sum([int(y) for y in str(x)])==num]
  return [li[0], li[-1]]
