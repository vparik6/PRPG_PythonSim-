#status: TODO: class holding register values

class registers():
    #r now holds the values of the registers, and the index will be the register number
    #0-7 will just end up being ignored (always 0) but that shouldn't mess anything up
    #so if you want to use these you do objectname.r[8] -- which would mean the contents of $8
    r = [0,0,0,0]
    PC = 0

    def print(self):    #print the register name and contents
        for i in range(0,4):
            if (self.r[i] != 0):
                print('$' + str(i) + ": " + str(self.r[i]))
        print('PC: ' + str(self.PC))
        return


class memory():
    '''
    the way these are accessed is that a function finds the
    index of a given number in the address array, then that
    index is used for the val array to store whatever goes in memory
    e.g.: memory.val[memory.addr.index(addr_index + offset)
    where memory is an object of this class
    '''

    addr = [0x2000,0x2004,0x2008,0x200C,
            0x2010,0x2014,0x2018,0x201C,
            0x2020,0x2024,0x2028,0x202C,
            0x2030,0x2034,0x2038,0x203C,
            0x2040,0x2044,0x2048,0x204C,
            0x2050,0x2054,0x2058,0x205C,]
    val = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
           0,0,0,0,0,0]
    def print(self): #print the name and contents of memory
       for i in range(24):
           if (self.val[i] !=0):
               print(hex(self.addr[i]) + '\t' + str(self.val[i]))
       return



#Instruction class/object
#status: will need to modify to include what instructions we choose
class instr_parsed():

    def __init__(self, num):
        #the following are temporary lists which will correspond to all of the possible instructions
        r_type_opcodes = ['0100','0101','0110','0111','1000','1001','1010','1011','1100','1101','1110']
        r_type_funcs = ['add', 'addu','sub','slt','and','sltu','or','xor'] #decide what instructions these will be

        i_type_opcodes = ['0000','0001','0010','0011']   #i-type that will have only 1 register and immediate
        i_type_funcs = ['add',''] #decide what instructions these will be

        j_type_opcodes = ['1111']
        j_type_funcs = ['j']

        converted = format(num, '0{}b'.format(32))  #this will take the hex input,
        self.binary = converted                                            #convert it to 32-bit bitstring (no 0b prefix)
        #parsing, mostly self-explanatory by the attribute naming:
        self.op_prefix = converted[0:4]     #op_prefix to determine the type
        self.rd = int(converted[4:6], 2)    #destination register
        self.rs = int(converted[6:8],2)     #secondary register
        self.imm = int(converted[4:8])      #immediate value


        if self.op_prefix in r_type_opcodes:
            self.type = 'r_type'
            self.func = r_type_funcs[r_type_opcodes.index(self.op_prefix)]

        elif self.op_prefix in i_type_opcodes:  #if type i of typical sw format
            self.type = 'i_type'
            self.func = i_type_funcs[i_type_opcodes.index(self.op_prefix)]


        elif self.op_prefix in j_type_opcodes:  #if type i of the addi format
            self.type = 'j_type'
            self.func = j_type_funcs[j_type_opcodes.index(self.op_prefix)]
            #print(self.addr)
        else:
            self.type = 'error'

    def twos_comp(self, num): #I beleive for this project we can ignore negative numbers, per some instructor notes in piazza. Leaving the function here just in case.
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

    def get_string(self):   #still needs to be modified but will print the instruction in pseudocode format
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
    #function to  the instruction in pseudo-code FIXME: needs to be modified for project 3
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
