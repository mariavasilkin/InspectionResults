def get_file(filename):
    l=[]
    for line in open(filename).readlines():
        l.append(line.strip().split(','))
        return l


def print_grades():
    inspectiondata = get_file('Results_Without_Violations.csv')
    i = 0
    for list in inspectiondata: 
        if list[1]=='QUEENS':
            if i < 5:
                grade=int(list[8])
                print grade
                i = i + 1


print_grades()
