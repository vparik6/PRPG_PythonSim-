import numpy as np

class registers():
    #r now holds the values of the registers, and the index will be the register number
    #0-7 will just end up being ignored (always 0) but that shouldn't mess anything up
    #so if you want to use these you do objectname.r[8] -- which would mean the contents of $8
    r = [0,8,0,0,0,61440,15,-7,-38,-3,-4]
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

    addr = [0,1,2,3,
            4,5,6,7,
            8,9,10,11,
            12,13,14,15,
            16,17,18,19,
            20,21,22,23,
            24,25,26,27,
            28,29,30,31,
            32,33,34,35,
            36,37,38,39,
            40,41,41,43]
    val = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
           0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
           0,0,0,0,0,0,0,0,0,0]
    def print(self): #print the name and contents of memory
       for i in range(24):
           if (self.val[i] !=0):
               print(hex(self.addr[i]) + '\t' + str(self.val[i]))
       return



#Instruction class/object
class instr_parsed():

    def __init__(self, num):
        #the following are temporary lists which will correspond to all of the possible instructions
        r_type_opcodes = ['0100','0101','0110','0111','1001','1100','1111','1010']
        r_type_funcs = ['sw','lw','mult','mask_top','or_r','add_r', 'zero','branch_nz'] #decide what instructions these will be

        i_type_opcodes = ['0000','0001','0010','0011','1000','1101','1110']   #i-type that will have only 1 register and immediate
        i_type_funcs = ['addi_r0','addi_r1','half_lui','andi_r3','srl','subi_r1','sub_count']


        #parsing, mostly self-explanatory by the attribute naming:
        self.op_prefix = num[0:4]     #op_prefix to determine the type
        self.rd = int(num[4:6], 2)    #destination register
        self.rs = int(num[6:8],2)     #secondary register
        self.imm = int(num[4:8],2)      #immediate value


        if self.op_prefix in r_type_opcodes:
            self.type = 'r_type'
            self.func = r_type_funcs[r_type_opcodes.index(self.op_prefix)]

        elif self.op_prefix in i_type_opcodes:  #if type i of typical sw format
            self.type = 'i_type'
            self.func = i_type_funcs[i_type_opcodes.index(self.op_prefix)]
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
        if (self.type == 'r_type'):
            return (self.func + str(self.rd) + str(self.rs))
        if (self.type == 'i_type'):
            return (self.func + ' $' + str(self.rd) + str(self.imm))

    #function to  the instruction in pseudo-code FIXME: needs to be modified for project 3
    def print_instr(self):
        if (self.type == 'r_type'):
            print(self.func + str(self.rd) + str(self.rs))
            return (self.func + str(self.rd) + str(self.rs))
        if (self.type == 'i_type'):
            print(self.func + str(self.rd) + str(self.rs))
            return (self.func + str(self.rd) + str(self.rs))
