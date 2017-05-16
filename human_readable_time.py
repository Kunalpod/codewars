#Kunal Gautam
#Codewars : @Kunalpod
#Problem name: Human Readable Time
#Problem level: 5 kyu

def make_readable(seconds):
    s = '{:0>2}'.format(seconds%60) 
    m = '{:0>2}'.format((seconds//60)%60)
    h = '{:0>2}'.format(seconds//3600)
    return ':'.join([h,m,s])
