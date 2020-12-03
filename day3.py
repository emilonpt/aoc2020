import csv

def d3p1():

    with open('d3p1.csv') as file: #read input from csv
        reader = csv.reader(file)
        data = list(reader)

        data = [item[0] for item in data] #convert to list of strings

        current_x = 0
        current_y = 0
        tree_count = 0
        while current_y <= len(data)-1:

            if current_x > 30 :
                current_x -= 31

            terrain = data[current_y][current_x]

            if terrain == "#":
                tree_count += 1

            current_x += 3
            current_y += 1

        return tree_count

def d3p2():

    aux1 = d2aux(1,1)
    aux2 = d2aux(3,1)
    aux3 = d2aux(5,1)
    aux4 = d2aux(7,1)
    aux5 = d2aux(1,2)

    return (aux1*aux2*aux3*aux4*aux5)

def d2aux(xinc,yinc):
    with open('d3p1.csv') as file: #read input from csv
        reader = csv.reader(file)
        data = list(reader)

        data = [item[0] for item in data] #convert to list of strings

        current_x = 0
        current_y = 0
        tree_count = 0
        while current_y <= len(data)-1:

            if current_x > 30 :
                current_x -= 31

            terrain = data[current_y][current_x]

            if terrain == "#":
                tree_count += 1

            current_x += xinc
            current_y += yinc

        return tree_count



if __name__ == "__main__":
    #print(d3p1())
    print(d3p2())