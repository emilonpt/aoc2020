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

        res = get_bags_num(bags,'shiny gold')

        return res

def get_bags_num(bags, parent_bag, sum=0,mult=1,level=""):
    level += "." #before each print message, just for "debugging"
    try:
        for child in bags[parent_bag]:

            sum += int(child['q']) * int(mult)

            #print('\n{}Added {} bag(s) corresponding to {} child {} to parent {} (this considers a multiplier of {})'.format(level,int(child['q'])*int(mult),child['q'],child['b'],parent_bag,mult))
            #print('{}Sum is now {}'.format(level,sum))
            if child['b'] in bags:
                mult = int(child['q'])*mult
                #print('\n{}Will now add {} child bags to sum using a multiplier of {}:'.format(level,child['b'],mult))
            
                sum += get_bags_num(bags, child['b'], 0,mult,level)

            else:
                #print('\n{}{} has no children so sum does not change.\n'.format(level,child['b']))
                pass

    except KeyError:
        pass
    #print(level, sum)
    return sum

if __name__ == "__main__":
    #DO NOT uncomment more than 1 of these at the same time - for some reason they're not independent
    #haven't looked into why
    #print(d7p2('test1.csv'))#should output 32
    #print(d7p2('test2.csv'))#should output 126
    #print(d7p2('input.csv'))#should output answer
    pass