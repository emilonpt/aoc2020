import csv

def d2p1():

    with open('d2p1.csv') as file: #read input from csv
        reader = csv.reader(file)
        data = list(reader)
        
        data = [item[0] for item in data] #convert to list of strings

        valid_counter = 0

        for set in data:
            quantifier = set.split(':')[0]
            password = set.split(':')[1].split(' ')[1]
            minimum = int(quantifier.split('-')[0])
            maximum = int(quantifier.split('-')[1].split(' ')[0])
            letter = quantifier.split(' ')[1]

            if minimum <= password.count(letter) <= maximum:
                valid_counter += 1

        return valid_counter 

def d2p2():

    with open('d2p1.csv') as file: #read input from csv
        reader = csv.reader(file)
        data = list(reader)
        
        data = [item[0] for item in data] #convert to list of strings

        valid_counter = 0

        for set in data:
            position = set.split(':')[0]
            password = set.split(':')[1].split(' ')[1]
            PosA = int(position.split('-')[0])
            PosB = int(position.split('-')[1].split(' ')[0])
            letter = position.split(' ')[1]

            if ((password[PosA-1] == letter and password[PosB-1] != letter) or (password[PosA-1] != letter and password[PosB-1] == letter)):
                valid_counter += 1

        return valid_counter 


if __name__ == "__main__":
    #print(d2p1())
    print(d2p2())