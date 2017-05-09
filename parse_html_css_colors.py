#Kunal Gautam
#Codewars : @Kunalpod
#Problem name: Parse HTML/CSS Colors
#Problem level: 6 kyu

def parse_html_color(color):
    str=color[1:]
    if color[0]=='#':
        if len(color[1:])==3:
            str= color[1]+color[1]+color[2]+color[2]+color[3]+color[3]
    else: str=PRESET_COLORS[color.lower()][1:]
    
    return {'r':int(str[0:2],16),'g':int(str[2:4],16),'b':int(str[4:6],16)}
