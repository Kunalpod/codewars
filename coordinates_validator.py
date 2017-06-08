#Kunal Gautam
#Codewars : @Kunalpod
#Problem name: Coordinates Validator
#Problem level: 4 kyu

import re
def is_valid_coordinates(coord):
    if re.fullmatch('[-]{0,1}[0-9]{1,2}([.][0-9]*){0,1},[ ]{0,1}[-]{0,1}[0-9]{1,3}([.][0-9]*){0,1}', coord):
        coord = [abs(float(x)) for x in coord.split(',')]
        if coord[0]>=0 and coord[0]<=90 and coord[1]>=0 and coord[1]<=180:
            return True
    return False
