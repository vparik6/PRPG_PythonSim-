#r-types

#status: done and checked
#required: yes
#arithmetic
def addu(instruction, registers):

    operand1 = registers.r[instruction.rs] #value in rs
    operand2 =  registers.r[instruction.rt] #value in rt

    registers.r[instruction.rd] = operand1 + operand2
    registers.PC += 4
    return registers

def adds(instruction, registers):

    operand1 = registers.r[instruction.rs] #value in rs
    operand2 =  registers.r[instruction.rt] #value in rt

    registers.r[instruction.rd] = operand1 + operand2
    registers.PC += 4
    return registers

#status: done and checked
#required: yes
#arithmetic
def sub(instruction, registers):
    operand1 = registers.r[instruction.rs] #value in rs
    operand2 =  registers.r[instruction.rt] #value in rt

    registers.r[instruction.rd] = operand1 - operand2
    registers.PC += 4
    return registers


#status: done and checked
#required: yes
#arithmetic
def slt(instruction, registers):
    operand1 = registers.r[instruction.rs] #value in rs
    operand2 =  registers.r[instruction.rt] #value in rt

    if operand1 < operand2:
        registers.r[instruction.rd] = 1 #set value to rd to 1
    else:
        registers.r[instruction.rd] = 0 #set value to rd to 0
    registers.PC += 4
    return registers

#status: done and checked
#required: yes
#logic
def and_r(instruction, registers):
    operand1 = registers.r[instruction.rs] #value in rs
    operand2 = registers.r[instruction.rt] #value in rt

    registers.r[instruction.rd] = operand1 & operand2
    registers.PC += 4
    return registers


#status: done and checked
#required: yes
#logic
def sll(instruction, registers):
    operand1 = registers.r[instruction.rt] #value in rt
    operand2 = instruction.sh #shifting value

    registers.r[instruction.rd] = operand1 << operand2
    registers.PC += 4
    return registers

#status: done and checked
#required: yes
#logic
def srl(instruction, registers):
    operand1 = registers.r[instruction.rt] #value in rt
    operand2 = instruction.sh #shifting value

    registers.r[instruction.rd] = operand1 >> operand2
    registers.PC += 4
    return registers
#status: TO DO
#required: just for our project
#logic
def andi(instruction, registers):
    operand1 = registers.r[instruction.rs]
    operand2 = instruction.imm

    registers.r[instruction.rt] = operand1 & operand2
    registers.PC += 4
    return registers

#status: TO DO
#just for our project
#logic
def xor(instruction, registers):
    operand1 = registers.r[instruction.rs] #value in rs
    operand2 = registers.r[instruction.rt] #value in rt
    registers.r[instruction.rd] = operand1 ^ operand2
    registers.PC += 4
    return registers

#i-types

def lui(instruction, registers):
    registers.r[instruction.rt] = instruction.imm << 4
    registers.PC += 4
    return registers

#status: test
#required: yes
def addi(instruction, registers):
    operand1 = registers.r[instruction.rs]
    operand2 = instruction.imm
    registers.r[instruction.rt] = operand1 + operand2
    registers.PC += 4
    return registers

def or_r(instruction, registers):
    operand1 = registers.r[instruction.rs]
    operand2 = registers.r[instruction.rt]

    registers.r[instruction.rd] = operand1 | operand2
    registers.PC += 4
    return registers


#status: test
#required: yes
#logic
def ori(instruction, registers):
    operand1 = registers.r[instruction.rs]
    operand2 = instruction.imm

    registers.r[instruction.rt] = operand1 | operand2
    registers.PC += 4
    return registers

#status: test
#required: yes
#branch
def beq(instruction, registers):
    operand1 = registers.r[instruction.rs]
    operand2 = registers.r[instruction.rt]

    if (operand1 == operand2):
        registers.PC += (4 + (instruction.imm << 2))
    else:
        registers.PC += 4
    return registers

#status: test
#required: yes
#branch
def bne(instruction, registers):
    operand1 = registers.r[instruction.rs]
    operand2 = registers.r[instruction.rt]

    if (operand1 != operand2):
        registers.PC += (4 + (instruction.imm << 2))
    else:
        registers.PC += 4
    return registers

#status: DONE
#required: yes
#memory
def lw(instruction, registers, memory):
    addr_index = registers.r[instruction.rs]
    offset = instruction.imm
    registers.r[instruction.rt] = memory.val[memory.addr.index(addr_index + offset)]
    registers.PC += 4
    return registers

#status: DONE
#required: yes
#memory
def sw(instruction, registers, memory):
    addr_index = registers.r[instruction.rs]
    offset = instruction.imm
    memory.val[memory.addr.index(addr_index + offset)] = registers.r[instruction.rt]
    registers.PC += 4
    return memory


#j-types
#need for project
#branch
def j(instruction, registers):
    registers.PC = (instruction.addr << 2)
    return registers
