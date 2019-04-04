
import objects
import instructions
from simulator import simulate

def main():
    my_registers = objects.registers()      # create registers object
    instr_list = []
    my_memory = objects.memory()
    filename = 'machine_s107.txt'

    print("loading instructions from " + filename)
    file = open(filename, 'r')  #open the instruction file
    i = 0
    #endofinstructions =
    for instr in file:
        if (instr == '\n' or instr[0] == '#'):
            continue
        #instr = instr[0:10]
        #print(instr)
        temp = objects.instr_parsed(instr)
        #temp.print_instr() #pseudocode translation
        instr_list.append(temp)
        i += 1
    instr_list.append(objects.instr_parsed('11111111'))
    simulate(instr_list, my_registers, my_memory)
    return
main()
