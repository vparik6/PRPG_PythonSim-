from instructions import *

#status: test
def simulate(instructions, register, memory):
    finished = False
    count = 0
    print('***Simulation started***')
    output = open('debugout.txt','w')
    while(not(finished)):
        count += 1
        current = instructions[register.PC]
        #current.print_instr()
        if (current.binary == '11111111'):
            finished = True
            print('***Simulation Finished***')
            continue
        elif (current.func == 'half_lui'):
            register = half_lui(current, register)
        elif (current.func == 'addi_r0'):
            register = addi_r0(current, register)
        elif (current.func == 'addi_r1'):
            register = addi_r1(current, register)
        elif (current.func == 'or_r'):
            register = or_r(current, register)
        elif (current.func == 'mult'):
            register = mult(current, register)
        elif (current.func == 'mask_top'):
            register = mask_top(current, register)
        elif (current.func == 'subi_r1'):
            register = subi_r1(current, register)
        elif (current.func == 'andi_r3'):
            register = andi_r3(current, register)
        elif (current.func == 'add_r'):
            register = add_r(current, register)
        elif (current.func == 'srl'):
            register = srl(current, register)
        elif (current.func == 'lw'):
            register = lw(current, register, memory)
        elif (current.func == 'sw'):
            memory = sw(current, register, memory)
        elif (current.func == 'branch_nz'):
            register = branch_nz(current, register)
            #register.print()
            #memory.print()
            #input('press enter')
        elif (current.func == 'count_reset'):
            register = count_reset(current, register)
        elif (current.func == 'sub_count'):
            register = sub_count(current, register)
        elif (current.func == 'zero'):
            register = zero(current, register)

    print('Instruction count:' + str(count))
    print('\nThe contents of the registers are:')
    register.print()
    print('\n The contents of the memory are:')
    memory.print()
    return
