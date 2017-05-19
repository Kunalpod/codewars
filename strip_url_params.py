#Kunal Gautam
#Codewars : @Kunalpod
#Problem name: Strip Url Params
#Problem level: 4 kyu

def strip_url_params(url, params_to_strip = []):
    url = url.split('?')
    try:
        c = []
        args = []
        for x in url[1].split('&'):
            if x[0] not in params_to_strip and x[0] not in c:
                c.append(x[0])
                args.append(x)      
        return '?'.join([url[0], '&'.join(args)])            
    except:    return url[0]
