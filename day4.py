import csv
import re

def d4p1():

    with open('d4p1.csv') as file: #read input from csv
        reader = csv.reader(file)
        data = list(reader)

    #this block results in the candidates list
    #which essentially contains each block of data condensed into a single standardized string
    #ugly logic regarding nextitem handles last passport
    candidates = []
    data_components = ''
    for c,item in enumerate(data):

        try:
            nextitem = data[c+1]
        except:
            nextitem = []
        if item == [] or nextitem == []:
            if nextitem == []:
                data_components+= item[0] + " "
            data_components = data_components[:-1] #remove space at end of string
            candidates.append(data_components)
            data_components = ''
        else:
            data_components+= item[0] + " "

    #create two lists (requirements, hardcoded and candidates, from strings)
    #if all required are in candidates, then it's valid
    valid_count = 0
    required_component_names = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl','pid']
    for candidate in candidates:
        is_valid = True
        candidate_component_names = [cc.split(':')[0] for cc in candidate.split(' ')]
        if candidate_component_names != ['']:
            if all(elem in candidate_component_names  for elem in required_component_names):
                valid_count+=1
    return valid_count

def d4p2():

    rules = {'byr':{'len':4,'min':1920,'max':2002},
             'iyr':{'len':4,'min':2010,'max':2020},
             'eyr':{'len':4,'min':2020,'max':2030},
             'hgt':{'cm':{'min':150,'max':193},'in':{'min':59,'max':76}},
             'hcl':{'len':7,'first':'#','valid':{'letters':'a-f','numbers':'0-9'}},
             'ecl':['amb',
                            'blu',
                            'brn',
                            'gry',
                            'grn',
                            'hzl',
                            'oth'],
             'pid':{'len':9}
             }

    candidates = get_candidates()

    valid_count = 0
    for candidate in candidates:
        is_valid = True
        candidate_components= [cc for cc in candidate.split(' ')]
        for component in candidate_components:
            component_name = component.split(':')[0]
            component_value = component.split(':')[1]
            if component_name in ['byr', 'iyr', 'eyr']:
                m = re.match('^\d{4}$', component_value)
                if not m:
                    is_valid = False
                elif int(component_value) > rules[component_name]['max'] or int(component_value) < rules[component_name]['min']:
                        is_valid = False
            
            elif component_name == 'hgt':
                m = re.match('^(\d+)(cm|in)$', component_value)
                if m:
                    digits,unit = m.groups()
                    if int(digits) < rules[component_name][unit]['min'] or int(digits) > rules[component_name][unit]['max']:
                        is_valid = False
                else:
                    is_valid = False
            
            elif component_name == 'hcl':
                m = re.match('^#[0-9|a-f]{6}$', component_value)
                if not m:
                    is_valid = False
            elif component_name == 'ecl':
                if component_value not in rules[component_name]:
                    is_valid = False
            elif component_name == 'pid':
                m = re.match('^\d{9}$', component_value)
                if not m:
                    is_valid = False
        if is_valid == True:
            valid_count += 1
    return valid_count

def get_candidates():
    #as per d4p1() but returns the list of candidates instead of the count
    with open('d4p1.csv') as file: #read input from csv
        reader = csv.reader(file)
        data = list(reader)

    #this block results in the candidates list
    #which essentially contains each block of data condensed into a single standardized string
    #ugly logic regarding nextitem handles last passport
    candidates = []
    data_components = ''
    for c,item in enumerate(data):

        try:
            nextitem = data[c+1]
        except:
            nextitem = []
        if item == [] or nextitem == []:
            if nextitem == []:
                data_components+= item[0] + " "
            data_components = data_components[:-1] #remove space at end of string
            candidates.append(data_components)
            data_components = ''
        else:
            data_components+= item[0] + " "

    #create two lists (requirements, hardcoded and candidates, from strings)
    #if all required are in candidates, then it's valid
    valid_count = 0
    returned_candidates = []
    required_component_names = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl','pid']
    for candidate in candidates:
        is_valid = True
        candidate_component_names = [cc.split(':')[0] for cc in candidate.split(' ')]
        if candidate_component_names != ['']:
            if all(elem in candidate_component_names  for elem in required_component_names):
                returned_candidates.append(candidate)
    return returned_candidates

if __name__ == "__main__":
   #print(d4p1())
   print(d4p2())