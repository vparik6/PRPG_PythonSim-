#r-types

#i-types
def half_lui(instruction, registers):
    registers.r[instruction.rt] = instruction.imm << 4
    registers.PC += 1
    return registers

def full_lui(instruction, registers):
    registers.r[instruction.rt] = instruction.imm << 8
    registers.PC += 1
    return registers

#status: test
#required: yes
def addi(instruction, registers):
    operand1 = registers.r[instruction.rs]
    operand2 = instruction.imm
    registers.r[instruction.rt] = operand1 + operand2
    registers.PC += 1
    return registers


#status: test
#required: yes
#logic
def ori(instruction, registers):
    operand1 = registers.r[instruction.rs]
    operand2 = instruction.imm

    registers.r[instruction.rt] = operand1 | operand2
    registers.PC += 1
    return registers


def andi(instruction, registers):
    operand1 = registers.r[instruction.rs]
    operand2 = instruction.imm

    registers.r[instruction.rt] = operand1 | operand2
    registers.PC += 1
    return registers

def subi(instruction, registers):
    operand1 = registers.r[instruction.rs]
    operand2 = instruction.imm

    registers.r[instruction.rt] = operand1 | operand2
    registers.PC += 1
    return registers

def add_r(instruction, registers):
    operand1 = registers.r[instruction.rs]
    operand2 = instruction.imm

    registers.r[instruction.rt] = operand1 | operand2
    registers.PC += 1
    return registers

def mult(instruction, registers):
    operand1 = registers.r[instruction.rs]
    operand2 = instruction.imm

    registers.r[instruction.rt] = operand1 | operand2
    registers.PC += 1
    return registers

def srl(instruction, registers):
    operand1 = registers.r[instruction.rs]
    operand2 = instruction.imm

    registers.r[instruction.rt] = operand1 | operand2
    registers.PC += 1
    return registers

def and(instruction, registers):
    operand1 = registers.r[instruction.rs]
    operand2 = instruction.imm

    registers.r[instruction.rt] = operand1 | operand2
    registers.PC += 1
    return registers

#status: DONE
#required: yes
#memory
def lw(instruction, registers, memory):
    addr_index = registers.r[instruction.rs]
    offset = instruction.imm
    registers.r[instruction.rt] = memory.val[memory.addr.index(addr_index + offset)]
    registers.PC += 1
    return registers

#status: DONE
#required: yes
#memory
def sw(instruction, registers, memory):
    addr_index = registers.r[instruction.rs]
    offset = instruction.imm
    memory.val[memory.addr.index(addr_index + offset)] = registers.r[instruction.rt]
    registers.PC += 1
    return memory
