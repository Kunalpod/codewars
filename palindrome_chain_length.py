#Kunal Gautam
#Codewars : @Kunalpod
#Problem name: Palindrome Chain Length
#Problem level: 5 kyu

def palindrome_chain_length(n):
    counter = 0
    while(1):
        if str(n) == str(n)[::-1]:    return counter
        n += int(str(n)[::-1])
        counter += 1
