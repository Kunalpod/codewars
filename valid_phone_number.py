#Kunal Gautam
#Codewars : @Kunalpod
#Problem name: Valid Phone Number
#Problem level: 6 kyu

import re
def validPhoneNumber(phoneNumber):
    return bool(re.match('[(][0-9][0-9][0-9][)] [0-9][0-9][0-9]-[0-9][0-9][0-9][0-9]', phoneNumber)) and len(phoneNumber)==14
