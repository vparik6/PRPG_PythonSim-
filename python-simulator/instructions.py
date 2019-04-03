#status: DONE
def half_lui(instruction, registers):
    registers.r[instruction.rt] = instruction.imm << 4
    registers.PC += 1
    return registers

#status: DONE
def addi_r0(instruction, registers):
    registers.r[0] = instruction.imm
    registers.PC += 1
    return registers

#status: TODO
def addi_r1(instruction, registers):
    operand1 = registers.r[instruction.rs]
    operand2 = instruction.imm
    registers.r[instruction.rt] = operand1 + operand2
    registers.PC += 1
    return registers

#status: TODO
def or_r(instruction, registers):
    operand1 = registers.r[instruction.rs]
    operand2 =
    registers.r[instruction.rt] = operand1 | operand2
    registers.PC += 1
    return registers

#status:TODO
def mult(instruction, registers):

    registers.PC += 1
    return registers

#status:TODO
def mask_top(instruction, registers):

    registers.PC += 1
    return registers

#status:TODO
def subi_r1(instruction, registers):
    operand1 = registers.r[instruction.rs]
    operand2 = instruction.imm

    registers.r[instruction.rt] = operand1 | operand2
    registers.PC += 1
    return registers

#status:TODO
def andi(instruction, registers):
    operand1 = registers.r[instruction.rs]
    operand2 = instruction.imm

    registers.r[instruction.rt] = operand1 | operand2
    registers.PC += 1
    return registers

#status:TODO
def add_r(instruction, registers):
    operand1 = registers.r[instruction.rs]
    operand2 = instruction.imm

    registers.r[instruction.rt] = operand1 | operand2
    registers.PC += 1
    return registers

#status:TODO
def srl(instruction, registers):
    operand1 = registers.r[instruction.rs]
    operand2 = instruction.imm

    registers.r[instruction.rt] = operand1 | operand2
    registers.PC += 1
    return registers

#status: TODO
def lw(instruction, registers, memory):
    addr_index = registers.r[instruction.rs]
    offset = instruction.imm
    registers.r[instruction.rt] = memory.val[memory.addr.index(addr_index + offset)]
    registers.PC += 1
    return registers

#status: TODO
def sw(instruction, registers, memory):
    addr_index = registers.r[instruction.rs]
    offset = instruction.imm
    memory.val[memory.addr.index(addr_index + offset)] = registers.r[instruction.rt]
    registers.PC += 1
    return memory

#status:TODO
def branch_nz(instruction, registers):
    pc += 1
    return registers

#status:TODO
def count_reset(instruction, registers):
    pc += 1
    return registers

#status:TODO
def sub_count(instruction, registers):
    pc += 1
    return registers

#status:TODO
def zero(instruction, registers):
    pc += 1
    return registers
