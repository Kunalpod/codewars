#Kunal Gautam
#Codewars : @Kunalpod
#Problem name: Range Extraction
#Problem level: 4 kyu

def create_string(final, series):
    if len(series) <= 2:
        final.append(','.join([str(x) for x in series]))
    else:
        final.append('-'.join([str(series[0]), str(series[-1])]))
    return final    

def solution(args):
    series = [args[0]];    final = []
    for i in range(1, len(args)):
        if args[i] - args[i-1] == 1:
            series.append(args[i])
        else:
            final = create_string(final, series)
            series = [args[i]]
    if series:
        final = create_string(final, series)
    return ','.join(final)
