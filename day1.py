import csv

def d1p1():

    with open('d1p1.csv') as file: #read input from csv
        reader = csv.reader(file)
        data = list(reader)


    data = [int(item[0]) for item in data ] #convert to integers

    for counter,item in enumerate(data): #loop through data
        subdata = data[counter+1:]
        for subitem in subdata: #loop through subset of data after the item we're currently in
            if item + subitem == 2020:  #find the items that sum 2020
                return item, subitem, item*subitem

def d1p2():

    with open('d1p1.csv') as file: #read input from csv
        reader = csv.reader(file)
        data = list(reader)

    data = [int(item[0]) for item in data ] #convert to integers

    for counter,item in enumerate(data): #loop through data
        subdata = data[counter+1:]
        for subcounter,subitem in enumerate(subdata): #loop through subset of data after the item we're currently in
            subdata2 = subdata[subcounter+1:]
            for subitem2 in subdata2:
                if item + subitem + subitem2 == 2020:
                    return item,subitem,subitem2,item*subitem*subitem2



if __name__ == "__main__":
    #print(d1p1())
    print(d1p2())

