
import group_12_p2_objects
import group_12_p2_instructions
from group_12_p2_simulator import simulate

def main():
    my_registers = group_12_p2_objects.registers()      # create registers object
    instr_list = []
    my_memory = group_12_p2_objects.memory()
    filename = 'group_12_p2_PRPG.txt'
    print("loading instructions from " + filename)
    file = open(filename, 'r')  #open the instruction file
    i = 0
    for instr in file:
        if (instr == '\n' or instr[0] == '#'):
            continue
        instr = instr[0:10]
        temp = group_12_p2_objects.instr_parsed(int(instr,16))
        temp.print_instr() #pseudocode translation
        instr_list.append(temp)
        instr_list.append('')
        instr_list.append('')
        instr_list.append('')
        i += 4
    simulate(instr_list, my_registers, my_memory)
    return
main()
