#Kunal Gautam
#Codewars : @Kunalpod
#Problem name: Pretty date
#Problem level: 6 kyu

def to_pretty(seconds):
    if seconds==0: return 'just now'
    elif seconds<60: return 'a second ago' if seconds==1 else str(seconds) + ' seconds ago'
    elif seconds<(60*60): return 'a minute ago' if seconds//60==1 else str(seconds//60) + ' minutes ago'
    elif seconds<(60*60*24): return 'an hour ago' if seconds//(60*60)==1 else str(seconds//(60*60)) + ' hours ago'
    elif seconds<(60*60*24*7): return 'a day ago' if seconds//(60*60*24)==1 else str(seconds//(60*60*24)) + ' days ago'
    else: return 'a week ago' if seconds//(60*60*24*7)==1 else str(seconds//(60*60*24*7)) + ' weeks ago'
