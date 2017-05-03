#Kunal Gautam
#Codewars : @Kunalpod
#Problem name: Stop gninnipS My sdroW!
#Problem level: 6 kyu

def spin_words(sentence):
    arr = sentence.split()
    for i in range(len(arr)):
        if len(arr[i])>=5:
            arr[i] = ''.join(list(reversed(arr[i])))
    return ' '.join(arr)
