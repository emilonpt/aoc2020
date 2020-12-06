import csv

def d6p1():

    with open('d6p1.csv') as file: #read input from csv
        reader = csv.reader(file)
        data = list(reader)

    #re-adapted this from day 4
    all_answers = []
    components = ''
    for c,item in enumerate(data):

        try:
            nextitem = data[c+1]
        except:
            nextitem = []
        if item == [] or nextitem == []:
            if nextitem == []:
                components+= item[0] + " "
            components = components[:-1] #remove space at end of string
            all_answers.append(components)
            components = ''
        else:
            components+= item[0] + " "
    all_answers = [value for value in all_answers if value != '']

    total_count = 0
    for answer in all_answers:
        answer = answer.replace(' ','')
        total_count+= len(list(set(answer)))
    return total_count

def d6p2():

    with open('d6p1.csv') as file: #read input from csv
        reader = csv.reader(file)
        data = list(reader)

    #re-adapted this from day 4
    all_answers = []
    components = ''
    for c,item in enumerate(data):

        try:
            nextitem = data[c+1]
        except:
            nextitem = []
        if item == [] or nextitem == []:
            if nextitem == []:
                components+= item[0] + " "
            components = components[:-1] #remove space at end of string
            all_answers.append(components)
            components = ''
        else:
            components+= item[0] + " "
    all_answers = [value for value in all_answers if value != '']

    total_count = 0
    for answer in all_answers:
        sub_answers = answer.split(' ')
        for sa in sub_answers:
            count = 0
            for char in sa:
                if all(char in c for c in sub_answers):
                    count+=1
        total_count+= count
    return total_count

if __name__ == "__main__":
    #print(d6p1())
    print(d6p2())