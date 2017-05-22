#Kunal Gautam
#Codewars : @Kunalpod
#Problem name: Disemvowel Trolls
#Problem level: 7 kyu

def disemvowel(string):
    return ''.join([letter for letter in string if letter.lower() not in ['a', 'e', 'i', 'o', 'u']])
