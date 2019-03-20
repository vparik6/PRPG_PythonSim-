from group_12_p2_instructions import *

#status: test
def simulate(instructions, register, memory):
    finished = False
    count = 0
    print('***Simulation started***')
    output = open('debugout.txt','w')
    while(not(finished)):
        count += 1
        current = instructions[register.PC]
        if (current.binary == '00010000000000001111111111111111'):
            finished = True
            print('***Simulation Finished***')
            continue
        elif (current.func == 'addu'):
            register = addu(current, register)
        elif (current.func == 'addi'):
            register = addi(current, register)
        elif (current.func == 'sub'):
            register = sub(current, register)
        elif (current.func == 'slt'):
            register = slt(current, register)
        elif (current.func == 'and'):
            register = and_r(current, register)
        elif (current.func == 'ori'):
            register = ori(current, register)
        elif (current.func == 'sll'):
            register = sll(current, register)
        elif (current.func == 'srl'):
            register = srl(current, register)
        elif (current.func == 'beq'):
            register = beq(current, register)
        elif (current.func == 'bne'):
            register = bne(current, register)
        elif (current.func == 'lw'):
            register = lw(current, register, memory)
        elif (current.func == 'sw'):
            memory = sw(current, register, memory)
        elif (current.func == 'add'):
            register = adds(current, register)
        elif (current.func == 'slti'):
            register = slti(current, register)
        elif (current.func == 'sltu'):
            register = sltu(current, register)
        elif (current.func == 'lui'):
            register = lui(current, register)
        elif (current.func == 'andi'):
            register = andi(current, register)
        elif (current.func == 'or'):
            register = or_r(current, register)
        elif (current.func == 'xor'):
            register = xor(current, register)
        elif (current.func == 'xori'):
            register = xori(current, register)
        elif (current.func == 'j'):
            register = j(current, register)

    print('Instruction count:' + str(count))
    print('\nThe contents of the registers are:')
    register.print()
    print('\n The contents of the memory are:')
    memory.print()
    return
