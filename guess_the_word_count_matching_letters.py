#Kunal Gautam
#Codewars : @Kunalpod
#Problem name: Guess the Word: Count Matching Letters
#Problem level: 7 kyu

def count_correct_characters(correct, guess):
    if len(correct) != len(guess):    raise()
    count = 0
    for i in range(len(correct)):
        if correct[i] == guess[i]:    count+=1
    return count
