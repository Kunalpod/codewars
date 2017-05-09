#Kunal Gautam
#Codewars : @Kunalpod
#Problem name: Where is my parent!?(cry)
#Problem level: 6 kyu

def find_children(dancing_brigade):
    return ''.join(sorted(sorted(dancing_brigade), key = lambda x: x.lower()))
