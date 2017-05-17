#Kunal Gautam
#Codewars : @Kunalpod
#Problem name: Where my anagrams at?
#Problem level: 5 kyu

def anagrams(word, words):
    return [x for x in words if sorted(x) == sorted(word)]
