#Kunal Gautam
#Codewars : @Kunalpod
#Problem name: Mix Fruit Juice
#Problem level: 6 kyu

def mix_fruit(arr):
    regular = ['banana', 'orange', 'apple', 'lemon', 'grapes']
    special = ['avocado', 'strawberry', 'mango']
    sum = 0
    for item in arr:
        if item.lower() in regular: sum += 5
        elif item.lower() in special: sum += 7
        else: sum+=9
    return round(sum/len(arr))
