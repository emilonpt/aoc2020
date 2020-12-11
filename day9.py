def d9p1():

    with open('d9p1.csv') as file: #read input from csv
        numbers = file.readlines()
        numbers = [int(s.strip()) for s in numbers]

        preamble_start = 0
        preamble_end = 25
        while True:

            preamble = numbers[preamble_start:preamble_end]
            after_preamble = numbers[preamble_end:]
            sums = []
            for c,p in enumerate(preamble):
                for cc,pp in enumerate(preamble[c+1:]):
                    sums.append(p+pp)
            
            first_after_p = after_preamble[0]

            if first_after_p not in sums:
                return first_after_p,numbers
            else:
                preamble_start+=1
                preamble_end +=1

def d9p2():

    d9p1_r = d9p1()
    target = d9p1_r[0]
    numbers = d9p1_r[1]
    sums = []
    
    for c,s in enumerate(numbers):
        print(c)
        nc = numbers[c:]
        for ss in enumerate(nc):
            for i in range(0,len(nc)):
                if target < sum(nc[0:i]):
                    break
                if target == sum(nc[0:i]):
                    return min(nc[0:i])+max(nc[0:i])


if __name__ == "__main__":
    print(d9p2())