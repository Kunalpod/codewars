#Kunal Gautam
#Codewars : @Kunalpod
#Problem name: Count of positives / sum of negatives
#Problem level: 7 kyu

def count_positives_sum_negatives(arr):
    return [len([x for x in arr if x>0]), sum([x for x in arr if x<0])] if arr else []
