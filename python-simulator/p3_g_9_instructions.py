#status: DONE
def half_lui(instruction, registers):
    registers.r[3] = instruction.imm << 4
    registers.PC += 1
    return registers

#status: DONE
def addi_r0(instruction, registers):
    registers.r[0] = instruction.imm
    registers.PC += 1
    return registers

#status: DONE
def addi_r1(instruction, registers):
    registers.r[1] = registers.r[1] + instruction.imm
    registers.PC += 1
    return registers

#status: DONE
def or_r(instruction, registers):
    registers.r[instruction.rd] = registers.r[instruction.rd] | registers.r[instruction.rs]
    registers.PC += 1
    return registers

#status:DONE
def mult(instruction, registers):
    registers.r[instruction.rd] = registers.r[instruction.rd] * registers.r[instruction.rs]
    registers.PC += 1
    return registers

#status: DONE
def mask_top(instruction, registers):
    registers.r[instruction.rd] = registers.r[5] & registers.r[instruction.rs]
    registers.PC += 1
    return registers

#status:DONE
def subi_r1(instruction, registers):
    registers.r[1] = registers.r[1] - instruction.imm
    registers.PC += 1
    return registers

#status:DONE
def andi_r3(instruction, registers):
    registers.r[3] = registers.r[3] & instruction.imm
    registers.PC += 1
    return registers

#status:DONE
def add_r(instruction, registers):
    registers.r[instruction.rd] = registers.r[instruction.rd] + registers.r[instruction.rs]
    registers.PC += 1
    return registers

#status:DONE
def srl(instruction, registers):
    #print(instruction.rs)
    if instruction.rs == 0:
        registers.r[instruction.rd] = registers.r[instruction.rd] >> 1
    elif instruction.rs == 2:
        registers.r[instruction.rd] = registers.r[instruction.rd] >> 4
    else:
        registers.r[instruction.rd] = registers.r[instruction.rd] >> 8
    registers.PC += 1
    #print('$2:' + str(registers.r[2]))
    #print('$3:' + str(registers.r[3]))
    return registers

#status: DONE
def lw(instruction, registers, memory):
    addr_index = registers.r[instruction.rs]
    registers.r[instruction.rd] = memory.val[memory.addr.index(addr_index)]
    registers.PC += 1
    #print('PC:' + str(registers.PC))
    #input('press enter')
    return registers

#status: DONE
def sw(instruction, registers, memory):
    addr_index = registers.r[instruction.rs]
    memory.val[memory.addr.index(addr_index)] = registers.r[instruction.rd]
    registers.PC += 1
    #print(hex(registers.r[1]))
    #input('press enter')
    return memory

#status:DONE
def branch_nz(instruction, registers):
    #print('PC:' + str(registers.PC))
    #print('immediate value ' +  str(instruction.imm) + ' contents: ' + str(registers.r[instruction.imm]))
    #if instruction.imm == 10:
        #print('$1: ' + str(registers.r[1]) + '\n' +'$2: ' + str(registers.r[2]) + '\n' + '$3: ' + str(registers.r[3]))
        #input('press enter')
    if registers.r[6] > 0:
        registers.PC += registers.r[instruction.imm]
    elif registers.r[6] == 0:
        registers.PC += 1
    return registers

#status:DONE
def count_reset(instruction, registers):
    registers.r[6] = 16
    registers.PC += 1
    return registers

#status:DONE
def sub_count(instruction, registers):
    registers.r[6] -= 1
    registers.PC += 1
    return registers

#status:DONE
def zero(instruction, registers):
    registers.r[instruction.rd] = 0
    registers.PC += 1
    #print('$' + str(instruction.rd) + ': ' + str(registers.r[instruction.rd]))
    #input('press enter')
    return registers
