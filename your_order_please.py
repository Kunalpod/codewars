#Kunal Gautam
#Codewars : @Kunalpod
#Problem name: Your order, please
#Problem level: 6 kyu

import re
def key(x):
    return int(re.sub("[a-zA-Z]+", "", x))

def order(sentence):
  return " ".join(sorted(sentence.split(), key = key))
