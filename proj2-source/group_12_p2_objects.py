#status: TODO: class holding register values

class registers():
    #r now holds the values of the registers, and the index will be the register number
    #0-7 will just end up being ignored (always 0) but that shouldn't mess anything up
    #so if you want to use these you do objectname.r[8] -- which would mean the contents of $8
    r = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    PC = 0

    def print(self):
        print('$0: 0')
        for i in range(8,24):
            if (self.r[i] != 0):
                print('$' + str(i) + ": " + str(self.r[i]))
        print('PC: ' + str(self.PC))
        return


class memory():
    #still needs to be done
    addr = [0x2000,0x2004,0x2008,0x200C,
            0x2010,0x2014,0x2018,0x201C,
            0x2020,0x2024,0x2028,0x202C,
            0x2030,0x2034,0x2038,0x203C,
            0x2040,0x2044,0x2048,0x204C,
            0x2050,0x2054,0x2058,0x205C,]
    val = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
           0,0,0,0,0,0]
    def print(self):
       for i in range(24):
           if (self.val[i] !=0):
               print(hex(self.addr[i]) + '\t' + str(self.val[i]))
       return



#Instruction class/object
#status: might be done?
class instr_parsed():
    def __init__(self, num):
        #the following are temporary lists which will correspond to all of the possible instructions
        r_type1_funcs = ['100000','100001','100010','101010','100100','101011','100101','100110']
        r_type1_opcodes = ['add', 'addu','sub','slt','and','sltu','or','xor']
        r_type2_funcs = ['000000','000010']    #r-type that will have 2 registers and shifting num
        r_type2_opcodes = ['sll','srl']

        i_type1_prefixes = ['101011','100011']   #i-type that will have only 1 register and immediate
        i_type1_opcodes = ['sw','lw']
        i_type2_prefixes = ['001000','001101','000100','000101','001010','001100','001110']   #i-type that will have 2 registers and immediate
        i_type2_opcodes = ['addi', 'ori','beq','bne','slti','andi','xori']
        i_type3_prefixes = ['001111']
        i_type3_opcodes = ['lui']

        j_type_prefixes = ['000010']
        j_type_opcodes = ['j']

        converted = format(num, '0{}b'.format(32))  #this will take the hex input,
        self.binary = converted                                            #convert it to 32-bit bitstring (no 0b prefix)
        #parsing, mostly self-explanatory by the attribute naming:
        self.op_prefix = converted[0:6]     #op_prefix to determine the type
        self.rs = int(converted[6:11], 2)
        self.rt = int(converted[11:16],2)
        self.rd = int(converted[16:21],2)
        #print(converted)
        self.sh = int(converted[21:26],2)
        self.imm = self.twos_comp(converted[16:32])  #FIXME call twos_comp(converted[16:32])
                                                   #here, should return a signed int
        self.func = converted[26:32]        #function code of what instruction it is exactly
        if self.op_prefix == '000000':
            if self.func in r_type1_funcs:  #if type r uses three registers
                self.type = 'r_type1'
                self.func = r_type1_opcodes[r_type1_funcs.index(self.func)]
            elif self.func in r_type2_funcs:  #if type r uses 2 registers and shifts
                self.type = 'r_type2'
                self.func = r_type2_opcodes[r_type2_funcs.index(self.func)]

        #note we need to distinguish between two types of type i instructions
        elif self.op_prefix in i_type1_prefixes:  #if type i of typical sw format
            self.type = 'i_type1'
            self.func = i_type1_opcodes[i_type1_prefixes.index(self.op_prefix)]
            #if int(self.imm) == 0:
            #    self.imm = None
        elif self.op_prefix in i_type2_prefixes:  #if type i of the addi format
            self.type = 'i_type2'
            self.func = i_type2_opcodes[i_type2_prefixes.index(self.op_prefix)]
        elif self.op_prefix in i_type3_prefixes:  #if type i of the addi format
            self.type = 'i_type3'
            self.func = i_type3_opcodes[i_type3_prefixes.index(self.op_prefix)]

        elif self.op_prefix in j_type_prefixes:  #if type i of the addi format
            self.type = 'j_type'
            self.func = j_type_opcodes[j_type_prefixes.index(self.op_prefix)]
            self.addr = int(converted[6:32], 2)
            #print(self.addr)
        else:
            self.type = 'error'
        if (self.func == 'ori'):
            self.imm = int(converted[16:32])
    def twos_comp(self, num):
        val = num
        if num[0] == '1':
            temp_val = int(num, 2)
            temp_val -= 1
            num = format(temp_val, '0{}b'.format(16))
            temp_list = list(num)
            num = ''
            for i in range(0,len(temp_list)):
                if temp_list[i] == '0':
                    num += '1'
                else:
                    num += '0'
            return -int(num, 2)
        return int(num,2)
    def get_string(self):
        if (self.type == 'r_type1'):

            return (self.func + ' $' + str(self.rd) + ', $' + str(self.rs) + ', $' + str(self.rt))
        if (self.type == 'r_type2'):

            return (self.func + ' $' + str(self.rd) + ', $' + str(self.rt) + ', ' + str(self.sh))
        if (self.type == 'i_type1'):

            return (self.func + ' $' + str(self.rt) + ', ' + str(self.imm) + '($' + str(self.rs) + ')')
        if (self.type == 'i_type2'):

            return (self.func + ' $' + str(self.rt) + ', $' + str(self.rs) + ', ' + str(self.imm))
        if (self.type == 'i_type3'):

            return (self.func + ' $' + str(self.rt) + ', $' + str(self.imm))
        if (self.type == 'j_type'):

            return (self.func + ' ' + str(self.addr))
    #function to  the instruction in pseudo-code
    def print_instr(self):
        if (self.type == 'r_type1'):
            print(self.func + ' $' + str(self.rd) + ', $' + str(self.rs) + ', $' + str(self.rt))
            return (self.func + ' $' + str(self.rd) + ', $' + str(self.rs) + ', $' + str(self.rt))
        if (self.type == 'r_type2'):
            print(self.func + ' $' + str(self.rd) + ', $' + str(self.rt) + ', ' + str(self.sh))
            return (self.func + ' $' + str(self.rd) + ', $' + str(self.rt) + ', ' + str(self.sh))
        if (self.type == 'i_type1'):
            print(self.func + ' $' + str(self.rt) + ', ' + str(self.imm) + '($' + str(self.rs) + ')')
            return (self.func + ' $' + str(self.rt) + ', ' + str(self.imm) + '($' + str(self.rs) + ')')
        if (self.type == 'i_type2'):
            print(self.func + ' $' + str(self.rt) + ', $' + str(self.rs) + ', ' + str(self.imm))
            return (self.func + ' $' + str(self.rt) + ', $' + str(self.rs) + ', ' + str(self.imm))
        if (self.type == 'i_type3'):
            print(self.func + ' $' + str(self.rt) + ', ' + str(self.imm))
            return (self.func + ' $' + str(self.rt) + ', ' + str(self.imm))
        if (self.type == 'j_type'):
            print(self.func + ' ' + str(self.addr))
            return (self.func + ' ' + str(self.addr))
