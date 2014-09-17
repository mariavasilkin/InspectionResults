

def get_file(filename):
    l=[]
    for line in open(filename).readlines():
        l.append(line.strip().split(','))
    return l
    
inspectiondata = get_file('Results_Without_violations.csv')


def borough_data(boro,col):
    '''
    boro is a string, col is either 3 (food type) or 6 (grade)
    '''
    d = {}
    for list in inspectiondata:
        if list[1]==boro:
            if d.has_key(list[col]):
                d[list[col]]+=1
            else:
                d[list[col]]=1
    return d

print borough_data("QUEENS",3)
