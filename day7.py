import re
import functools 


def d7p1():

    with open('d7p1.csv') as file: #read input from csv
        rules = file.readlines()
        rules = [s.strip() for s in rules]

        bag_types = dict()

        for rule in rules:
            bag_types[rule.split(' ')[0]+' '+rule.split(' ')[1]] = [b for b in rule.split(' contain ')[1].split(',')] # populate dict
        
        #clean dict
        for bagtype in bag_types.values():
            for c,i in enumerate(bagtype):
                bagtype[c] = i.strip(".").strip('bags').lstrip().rstrip() #strip dots and spaces
                bagtype[c] = re.sub(r'\d\s','',bagtype[c])#remove quantity, not needed for this purpose

        #solve part1

        targets =  ['shiny gold']
        result = len(list(set(get_bags(targets,bag_types))))

        return result

def get_bags(targets,bag_types,results=[]):
    holders = []
    for rule in bag_types:
        for bag in targets:
            if bag in bag_types[rule]:
                holders.append(rule)
                results.append(rule)
    if holders == []:
        return results
    if holders != []:
        return get_bags(holders,bag_types,results)

def get_bags_q(targets,bag_types,results=dict()):
    holdings = []
    for target in targets: 
        for holding in bag_types[target]:
            if holding['b'] != 'other':
                holdings.append(holding['b'])
                if target in results:
                    results[target].append(holding)
                else:
                    results[target] = [holding]
    if holdings == []:
        return results
    if holdings != []:
        return get_bags_q(holdings,bag_types,results)

def d7p2(inputfile):
    with open(inputfile) as file: #read input from csv
        rules = file.readlines()
        rules = [s.strip() for s in rules]

        bag_types = dict()

        for rule in rules:
            bag_types[rule.split(' ')[0]+' '+rule.split(' ')[1]] = [b for b in rule.split(' contain ')[1].split(',')] # populate dict
        
        #clean dict
        for bagtype in bag_types.values():
            for c,i in enumerate(bagtype):
                bagtype[c] = i.strip(".").strip('bags').lstrip().rstrip() #strip dots and spaces
                bagtype[c] = {'q':bagtype[c].split(' ')[0],'b':' '.join(bagtype[c].split(' ')[1:])}

        targets =  ['shiny gold']
        bags = get_bags_q(targets,bag_types)

        for b in bags:
            bags[b] = list({v['b']:v for v in bags[b]}.values()) # fix duplicates in bags

        res = get_bags_num(bags,'shiny gold')

        return res

def get_bags_num(bags, parent_bag, count_bags=0):
    try:
        for child in bags[parent_bag]:
            count_bags += int(child['q'])

            count_bags += get_bags_num(bags, child['b']) *int(child['q'])

    except KeyError:
        return 0
    return count_bags

if __name__ == "__main__":
    #print(d7p1())
    print(d7p2('d7p1.csv'))#should output answer

    pass