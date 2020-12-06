import csv

def d5p1():

    with open('d5p1.csv') as file: #read input from csv
        reader = csv.reader(file)
        data = list(reader)
        boarding_passes = [d[0] for d in data]

    tot_check = []
    for bp in boarding_passes:
        bp_row = range(0,128) #0 through 127
        bp_col = range(0,8) # 0 through 7

        for c,char in enumerate(bp[:7]):
            if char == 'F':
                bp_row = range(min(bp_row),int((max(bp_row)-min(bp_row))/2)+1+min(bp_row))
            elif char == 'B':
                bp_row = range(min(bp_row) + int((max(bp_row)-min(bp_row))/2)+1,max(bp_row)+1)
        bp_row = min(bp_row)

        for c,char in enumerate(bp[7:]):
            if char == 'L':
                bp_col = range(min(bp_col),int((max(bp_col)-min(bp_col))/2)+1+min(bp_col))
            elif char == 'R':
                bp_col = range(min(bp_col) + int((max(bp_col)-min(bp_col))/2)+1,max(bp_col)+1)
        bp_col = min(bp_col)
        
        tot_check.append(bp_row*8+bp_col)

    return max(tot_check)
            

def d5p2():
    sits = get_sits()
    all_sits = [(r,c) for r in range(0,128) for c in range(0,8)]
    sits_ids = [r*8+c for r,c in sits]
    candidates = []
    for sit in all_sits:
        if sit not in sits:
            candidates.append(sit)
    spot = ()
    for sit in candidates:
        sit_id = sit[0]*8+sit[1]
        if sit_id-1 in sits_ids and sit_id+1 in sits_ids:
            spot = sit
    return(spot,spot[0]*8+spot[1])


def get_sits():

    #similar to d5p1 but returns sits instead of max of tot_check

    with open('d5p1.csv') as file: #read input from csv
        reader = csv.reader(file)
        data = list(reader)
        boarding_passes = [d[0] for d in data]

    sits = []
    tot_check = []
    for bp in boarding_passes:
        bp_row = range(0,128) #0 through 127
        bp_col = range(0,8) # 0 through 7

        for c,char in enumerate(bp[:7]):
            if char == 'F':
                bp_row = range(min(bp_row),int((max(bp_row)-min(bp_row))/2)+1+min(bp_row))
            elif char == 'B':
                bp_row = range(min(bp_row) + int((max(bp_row)-min(bp_row))/2)+1,max(bp_row)+1)
        bp_row = min(bp_row)

        for c,char in enumerate(bp[7:]):
            if char == 'L':
                bp_col = range(min(bp_col),int((max(bp_col)-min(bp_col))/2)+1+min(bp_col))
            elif char == 'R':
                bp_col = range(min(bp_col) + int((max(bp_col)-min(bp_col))/2)+1,max(bp_col)+1)
        bp_col = min(bp_col)
        
        sits.append((bp_row,bp_col))

    return sits


if __name__ == "__main__":
    #print(d5p1())
    print(d5p2())
