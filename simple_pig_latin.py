#Kunal Gautam
#Codewars : @Kunalpod
#Problem name: Simple Pig Latin
#Problem level: 5 kyu

def pig_it(text):
    text1 = ' '.join([x[1:]+x[0]+'ay' for x in text.split()])
    return text1 if text1[-3].isalpha() else text1[:-2]
