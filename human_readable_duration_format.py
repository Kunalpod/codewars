#Kunal Gautam
#Codewars : @Kunalpod
#Problem name: Human readable duration format
#Problem level: 4 kyu

def format_duration(seconds):
    if not seconds:
        return "now"
    y = d = h = m = s = 0
    if seconds<60:
        s = seconds
    else:
        m = seconds//60
        s=seconds%60
        if m>=60:
            h = m//60
            m = m%60
            if h>=24:
                d = h//24
                h = h%24
                if d>=365:
                    y = d//365
                    d = d%365
                    
    if y!=0:
        if d!=0:  
            if h!=0:
                if m!=0:
                    if s!=0:
                        return str(y)+" year"+('s' if y>1 else '')+", "+str(d)+" day"+('s' if d>1 else '')+", "+str(h)+" hour"+('s' if h>1 else '')+", "+str(m)+" minute"+('s' if m>1 else '')+" and "+str(s)+" second"+('s' if s>1 else '')
                    else:
                        return str(y)+" year"+('s' if y>1 else '')+", "+str(d)+" day"+('s' if d>1 else '')+", "+str(h)+" hour"+('s' if h>1 else '')+" and "+str(m)+" minute"+('s' if m>1 else '')
                else:
                    if s!=0:
                        return str(y)+" year"+('s' if y>1 else '')+", "+str(d)+" day"+('s' if d>1 else '')+", "+str(h)+" hour"+('s' if h>1 else '')+" and "+str(s)+" second"+('s' if s>1 else '')
                    else:
                        return str(y)+" year"+('s' if y>1 else '')+", "+str(d)+" day"+('s' if d>1 else '')+" and "+str(h)+" hour"+('s' if h>1 else '')
            else:
                if m!=0:
                    if s!=0:
                        return str(y)+" year"+('s' if y>1 else '')+", "+str(d)+" day"+('s' if d>1 else '')+", "+str(m)+" minute"+('s' if m>1 else '')+" and "+str(s)+" second"+('s' if s>1 else '')
                    else:
                        return str(y)+" year"+('s' if y>1 else '')+", "+str(d)+" day"+('s' if d>1 else '')+" and "+str(m)+" minute"+('s' if m>1 else '')
                else:
                    if s!=0:
                        return str(y)+" year"+('s' if y>1 else '')+", "+str(d)+" day"+('s' if d>1 else '')+" and "+str(s)+" second"+('s' if s>1 else '')
                    else:
                        return str(y)+" year"+('s' if y>1 else '')+" and "+str(d)+" day"+('s' if d>1 else '')   
        else:
            if h!=0:
                if m!=0:
                    if s!=0:
                        return str(y)+" year"+('s' if y>1 else '')+", "+str(h)+" hour"+('s' if h>1 else '')+", "+str(m)+" minute"+('s' if m>1 else '')+" and "+str(s)+" second"+('s' if s>1 else '')
                    else:
                        return str(y)+" year"+('s' if y>1 else '')+", "+str(h)+" hour"+('s' if h>1 else '')+" and "+str(m)+" minute"+('s' if m>1 else '')
                else:
                    if s!=0:
                        return str(y)+" year"+('s' if y>1 else '')+", "+str(h)+" hour"+('s' if h>1 else '')+" and "+str(s)+" second"+('s' if s>1 else '')
                    else:
                        return str(y)+" year"+('s' if y>1 else '')+" and "+str(h)+" hour"+('s' if h>1 else '')
            else:
                if m!=0:
                    if s!=0:
                        return str(y)+" year"+('s' if y>1 else '')+", "+str(m)+" minute"+('s' if m>1 else '')+" and "+str(s)+" second"+('s' if s>1 else '')
                    else:
                        return str(y)+" year"+('s' if y>1 else '')+" and "+str(m)+" minute"+('s' if m>1 else '')
                else:
                    if s!=0:
                        return str(y)+" year"+('s' if y>1 else '')+" and "+str(s)+" second"+('s' if s>1 else '')
                    else:
                        return str(y)+" year"+('s' if y>1 else '') 
    else:
        if d!=0:  
            if h!=0:
                if m!=0:
                    if s!=0:
                        return str(d)+" day"+('s' if d>1 else '')+", "+str(h)+" hour"+('s' if h>1 else '')+", "+str(m)+" minute"+('s' if m>1 else '')+" and "+str(s)+" second"+('s' if s>1 else '')
                    else:
                        return str(d)+" day"+('s' if d>1 else '')+", "+str(h)+" hour"+('s' if h>1 else '')+" and "+str(m)+" minute"+('s' if m>1 else '')
                else:
                    if s!=0:
                        return str(d)+" day"+('s' if d>1 else '')+", "+str(h)+" hour"+('s' if h>1 else '')+" and "+str(s)+" second"+('s' if s>1 else '')
                    else:
                        return str(d)+" day"+('s' if d>1 else '')+" and "+str(h)+" hour"+('s' if h>1 else '')
            else:
                if m!=0:
                    if s!=0:
                        return str(d)+" day"+('s' if d>1 else '')+", "+str(m)+" minute"+('s' if m>1 else '')+" and "+str(s)+" second"+('s' if s>1 else '')
                    else:
                        return str(d)+" day"+('s' if d>1 else '')+" and "+str(m)+" minute"+('s' if m>1 else '')
                else:
                    if s!=0:
                        return str(d)+" day"+('s' if d>1 else '')+" and "+str(s)+" second"+('s' if s>1 else '')
                    else:
                        return str(d)+" day"+('s' if d>1 else '')   
        else:
            if h!=0:
                if m!=0:
                    if s!=0:
                        return str(h)+" hour"+('s' if h>1 else '')+", "+str(m)+" minute"+('s' if m>1 else '')+" and "+str(s)+" second"+('s' if s>1 else '')
                    else:
                        return str(h)+" hour"+('s' if h>1 else '')+" and "+str(m)+" minute"+('s' if m>1 else '')
                else:
                    if s!=0:
                        return str(h)+" hour"+('s' if h>1 else '')+" and "+str(s)+" second"+('s' if s>1 else '')
                    else:
                        return str(h)+" hour"+('s' if h>1 else '')
            else:
                if m!=0:
                    if s!=0:
                        return str(m)+" minute"+('s' if m>1 else '')+" and "+str(s)+" second"+('s' if s>1 else '')
                    else:
                        return str(m)+" minute"+('s' if m>1 else '')
                else:
                    if s!=0:
                        return str(s)+" second"+('s' if s>1 else '')
                    else:
                        return None 
