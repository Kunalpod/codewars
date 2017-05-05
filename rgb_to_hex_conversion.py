#Kunal Gautam
#Codewars : @Kunalpod
#Problem name: RGB To Hex Conversion
#Problem level: 5 kyu

def rgb(r, g, b):
    if r<0: r = 0
    if g<0: g = 0
    if b<0: b = 0
    if r>255: r = 255
    if g>255: g = 255
    if b>255: b = 255
    return ((hex(r)[2:] if len(hex(r))>3 else '0'+hex(r)[2:]) + (hex(g)[2:] if len(hex(g))>3 else '0'+hex(g)[2:]) + (hex(b)[2:] if len(hex(b))>3 else '0'+hex(b)[2:])).upper()
