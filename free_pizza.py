#Kunal Gautam
#Codewars : @Kunalpod
#Problem name: Free Pizza
#Problem level: 6 kyu

def pizza_rewards(customers, min_orders, min_price):
    return [key for key in customers if len([x for x in customers[key] if x >= min_price]) >= min_orders]
