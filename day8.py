global result

result = 0

def d8p1():

    with open('d8p1.csv') as file: #read input from csv
        instructions = file.readlines()
        instructions = [s.strip() for s in instructions]
        #print(instructions)
    
    accumulator = 0
    instruction_counter = [{'instruction':i,'times_exec':0} for i in instructions]

    id = 0
    i = instructions[id]
    operation = i.split(' ')[0]
    argument = int(i.split(' ')[1])
    process(operation,argument,id,accumulator,instructions,instruction_counter)
    return result[2]

def process(operation,argument,id,accumulator,instructions,instruction_counter):
    global result 

    instruction_counter[id]['times_exec'] += 1
    #print(instructions[id],id,accumulator,instruction_counter[id]['times_exec'])

    if instruction_counter[id]['times_exec'] > 1:
        if not result:
            result = instructions[id],id,accumulator,instruction_counter[id]['times_exec']
        return None

    try:
    
        if operation == "nop":
            operation = instructions[id+1].split(' ')[0]
            argument = int(instructions[id+1].split(' ')[1])
            id += 1
            process(operation,argument,id,accumulator,instructions,instruction_counter)
        
        if operation == "acc":
            accumulator += argument
            operation = instructions[id+1].split(' ')[0]
            argument = int(instructions[id+1].split(' ')[1])
            id += 1
            process(operation,argument,id,accumulator,instructions,instruction_counter)

        if operation == "jmp":
            orig_argument = int(argument)
            operation = instructions[id+orig_argument].split(' ')[0]
            argument = int(instructions[id+orig_argument].split(' ')[1])
            id += int(orig_argument)
            process(operation,argument,id,accumulator,instructions,instruction_counter)
    except IndexError:
        
        if not result:
            result = instructions[id],id,accumulator,instruction_counter[id]['times_exec']
        return None

    return None

def d8p2():
    global result
    with open('d8p1.csv') as file: #read input from csv
        instructions = file.readlines()
        instructions = [s.strip() for s in instructions]
        orig_instructions = list(instructions)
        #print(instructions)
        

    for c,instruction in enumerate(orig_instructions):
        instructions = list(orig_instructions)
        try:

            if instruction.split(' ')[0] == 'jmp':
                instructions[c] = instruction.replace('jmp','nop')
                instruction_counter = [{'instruction':i,'times_exec':0} for i in instructions]
                result = None
                accumulator = 0
                id = 0
                i = instructions[id]
                operation = i.split(' ')[0]
                argument = int(i.split(' ')[1])
                process(operation,argument,id,accumulator,instructions,instruction_counter)
                if int(result[1]) == len(instructions)-1:
                    print('((instruction,id,accumulator,times_exec), finished)')
                    return result, int(result[1]) == len(instructions)-1

            elif instruction.split(' ')[0] == 'nop':
                instructions[c] = instruction.replace('nop','jmp')
                instruction_counter = [{'instruction':i,'times_exec':0} for i in instructions]
                result = None
                accumulator = 0
                id = 0
                i = instructions[id]
                operation = i.split(' ')[0]
                argument = int(i.split(' ')[1])
                process(operation,argument,id,accumulator,instructions,instruction_counter)
                if int(result[1]) == len(instructions)-1:
                    print('((instruction,id,accumulator,times_exec), finished)')
                    return result, int(result[1]) == len(instructions)-1

        except IndexError:
            pass

if __name__ == "__main__":
    #print(d8p1())
    print(d8p2())