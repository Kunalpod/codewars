#Kunal Gautam
#Codewars : @Kunalpod
#Problem name: Simple Fun #270: Evil Code Medal
#Problem level: 7 kyu

def get_sec(time):
    return time[0]*3600 + time[1]*60 + time[2]

def evil_code_medal(user_time, gold, silver, bronze):
    user_time = get_sec(user_time.split(':'))
    gold = get_sec(gold.split(':'))
    silver = get_sec(silver.split(':'))
    bronze = get_sec(bronze.split(':'))
    if user_time < gold: return "Gold"
    elif user_time < silver: return "Silver"
    elif user_time < bronze: return "Bronze"
    else:    return "None"
