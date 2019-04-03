# this script will take MIPS code and output our kind of machine code
# for the instructions we have decided to support

fin = open('PRPG.txt')
fout = open('machine.txt', 'w')

for line in fin:
    if line != '\n' and line[0] != '#':
        args = line.split()
        #print(args[0])

        if args[0] == 'addi':
            opcode = 'opcode'
            register = args[1][1]
            print(register)
            imm = args[3]
            print(imm)
            #process registers (and immediate if i-type)
            #then convert to binary and write out to file
            fout.write(opcode + format(int(register), '0{}b'.format(2)) + format(int(imm), '0{}b'.format(4))) #FIXME
            fout.write('\n')
        elif args[0] == 'lui':
            opcode = ''
            #process registers (and immediate if i-type)
            #then convert to binary and write out to file
            fout.write('lui') #FIXME
            fout.write('\n')
        elif args[0] == 'andi':
            opcode = ''
            #process registers (and immediate if i-type)
            #then convert to binary and write out to file
            fout.write('andi') #FIXME
            fout.write('\n')
        elif args[0] == 'subi':
            opcode = ''
            #process registers (and immediate if i-type)
            #then convert to binary and write out to file
            fout.write('subi') #FIXME
            fout.write('\n')
        elif args[0] == 'add':
            opcode = ''
            #process registers (and immediate if i-type)
            #then convert to binary and write out to file
            fout.write('add') #FIXME
            fout.write('\n')
        elif args[0] == 'mult':
            opcode = ''
            #process registers (and immediate if i-type)
            #then convert to binary and write out to file
            fout.write('mult') #FIXME
            fout.write('\n')
        elif args[0] == 'sw':
            opcode = ''
            #process registers (and immediate if i-type)
            #then convert to binary and write out to file
            fout.write('sw') #FIXME
            fout.write('\n')
        elif args[0] == 'lw':
            opcode = ''
            #process registers (and immediate if i-type)
            #then convert to binary and write out to file
            fout.write('lw') #FIXME
            fout.write('\n')
        elif args[0] == 'srl':
            opcode = ''
            #process registers (and immediate if i-type)
            #then convert to binary and write out to file
            fout.write('srl') #FIXME
            fout.write('\n')
        elif args[0] == 'and':
            opcode = ''
            #process registers (and immediate if i-type)
            #then convert to binary and write out to file
            fout.write('and') #FIXME
            fout.write('\n')
        else:
            pass

fin.close()
fout.close()
