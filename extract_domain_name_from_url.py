#Kunal Gautam
#Codewars : @Kunalpod
#Problem name: Extract the domain name from a URL
#Problem level: 5 kyu

import re
def domain_name(url):
    url = re.split('www.', url)[1] if re.findall('www.', url) else re.split('://', url)[1]
    url = re.split('[.][a-z]+', url)[0]
    return url
