#Kunal Gautam
#Codewars : @Kunalpod
#Problem name: The Supermarket Queue
#Problem level: 6 kyu

def queue_time(customers, n):
    if not customers:    return 0
    li=customers[:n]
    for customer in customers[n:]:
        li[li.index(min(li))]+=customer
    return max(li)
