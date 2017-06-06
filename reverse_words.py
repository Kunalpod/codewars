#Kunal Gautam
#Codewars : @Kunalpod
#Problem name: Reverse words
#Problem level: 6 kyu

def reverse_words(s):
    words = s.split()
    for word in words:
        s = s.replace(word, word[::-1])
    return s
