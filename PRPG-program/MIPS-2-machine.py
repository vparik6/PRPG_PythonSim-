# this script will take MIPS code and output our kind of machine code
# for the instructions we have decided to support

fin = open('PRPGv2.txt')
fout = open('machine.txt', 'w')

for line in fin:
    if line != '\n' and line[0] != '#':
        args = line.split()
        #print(args[0])

        if args[0] == 'half_lui':
            opcode = '0010'
            imm= args[1]
            print(opcode + format(int(imm), '0{}b'.format(4)))
            fout.write(opcode + format(int(imm), '0{}b'.format(4)))
            fout.write('\n')
        elif args[0] == 'addi_r0':
            opcode = '0000'
            imm= args[1]
            print(opcode + format(int(imm), '0{}b'.format(4)))
            fout.write(opcode + format(int(imm), '0{}b'.format(4)))
            fout.write('\n')
        elif args[0] == 'addi_r1':
            opcode = '0001'
            imm= args[1]
            print(opcode + format(int(imm), '0{}b'.format(4)))
            fout.write(opcode + format(int(imm), '0{}b'.format(4)))
            fout.write('\n')
        elif args[0] == 'or_r':
            opcode = '1001'
            rd = args[1]
            rs = args[2]
            print(opcode + format(int(rd), '0{}b'.format(2)) + format(int(rs), '0{}b'.format(2)))
            fout.write(opcode + format(int(rd), '0{}b'.format(2)) + format(int(rs), '0{}b'.format(2)))
            fout.write('\n')
        elif args[0] == 'mult':
            opcode = '0110'
            rd = args[1]
            rs = args[2]
            print(opcode + format(int(rd), '0{}b'.format(2)) + format(int(rs), '0{}b'.format(2)))
            fout.write(opcode + format(int(rd), '0{}b'.format(2)) + format(int(rs), '0{}b'.format(2)))
            fout.write('\n')
        elif args[0] == 'mask_top':
            opcode = '0111'
            rd = args[1]
            rs = args[2]
            print(opcode + format(int(rd), '0{}b'.format(2)) + format(int(rs), '0{}b'.format(2)))
            fout.write(opcode + format(int(rd), '0{}b'.format(2)) + format(int(rs), '0{}b'.format(2)))
            fout.write('\n')
        elif args[0] == 'subi_r1':
            opcode = '1101'
            imm= args[1]
            print(opcode + format(int(imm), '0{}b'.format(4)))
            fout.write(opcode + format(int(imm), '0{}b'.format(4)))
            fout.write('\n')
        elif args[0] == 'andi_r3':
            opcode = '0011'
            imm= args[1]
            print(opcode + format(int(imm), '0{}b'.format(4)))
            fout.write(opcode + format(int(imm), '0{}b'.format(4)))
            fout.write('\n')
        elif args[0] == 'add_r':
            opcode = '1100'
            rd = args[1]
            rs = args[2]
            print(opcode + format(int(rd), '0{}b'.format(2)) + format(int(rs), '0{}b'.format(2)))
            fout.write(opcode + format(int(rd), '0{}b'.format(2)) + format(int(rs), '0{}b'.format(2)))
            fout.write('\n')
        elif args[0] == 'srl':
            opcode = '1000'
            rd = args[1]
            rs = args[2]
            print(opcode + format(int(rd), '0{}b'.format(2)) + format(int(rs), '0{}b'.format(2)))
            fout.write(opcode + format(int(rd), '0{}b'.format(2)) + format(int(rs), '0{}b'.format(2)))
            fout.write('\n')
        elif args[0] == 'lw':
            opcode = '0101'
            rd = args[1]
            rs = args[2]
            print(opcode + format(int(rd), '0{}b'.format(2)) + format(int(rs), '0{}b'.format(2)))
            fout.write(opcode + format(int(rd), '0{}b'.format(2)) + format(int(rs), '0{}b'.format(2)))
            fout.write('\n')
        elif args[0] == 'sw':
            opcode = '0100'
            rd = args[1]
            rs = args[2]
            print(opcode + format(int(rd), '0{}b'.format(2)) + format(int(rs), '0{}b'.format(2)))
            fout.write(opcode + format(int(rd), '0{}b'.format(2)) + format(int(rs), '0{}b'.format(2)))
            fout.write('\n')
        elif args[0] == 'branch_nz':
            opcode = '1010'
            imm= args[1]
            print(opcode + format(int(imm), '0{}b'.format(4)))
            fout.write(opcode + format(int(imm), '0{}b'.format(4)))
            fout.write('\n')
        elif args[0] == 'count_reset':
            opcode = '1011'
            print(opcode + '0000')
            fout.write(opcode + format(int(imm), '0{}b'.format(4)))
            fout.write('\n')
        elif args[0] == 'sub_count':
            opcode = '1110'
            print(opcode + '0000')
            fout.write(opcode + format(int(imm), '0{}b'.format(4)))
            fout.write('\n')
        elif args[0] == 'zero':
            opcode = '1111'
            rd = args[1]
            rs = args[2]
            print(opcode + format(int(rd), '0{}b'.format(2)) + '00')
            fout.write(opcode + format(int(rd), '0{}b'.format(2)) + '00')
            fout.write('\n')

        else:
            pass

fin.close()
fout.close()
