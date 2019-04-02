# this script will take MIPS code and output our kind of machine code
# for the instructions we have decided to support

fin = open('PRPG.txt')
fout = open('machine.txt', 'w')

for line in fin:
    args = line.split()

    if args[0] == 'addi':
        #process registers (and immediate if i-type)
        #then convert to binary and write out to file
        fout.write() #FIXME
    elif args[0] == 'lui':
        #process registers (and immediate if i-type)
        #then convert to binary and write out to file
        fout.write() #FIXME
    elif args[0] == 'andi':
        #process registers (and immediate if i-type)
        #then convert to binary and write out to file
        fout.write() #FIXME
    elif args[0] == 'subi':
        #process registers (and immediate if i-type)
        #then convert to binary and write out to file
        fout.write() #FIXME
    elif args[0] == 'add':
        #process registers (and immediate if i-type)
        #then convert to binary and write out to file
        fout.write() #FIXME
    elif args[0] == 'mult':
        #process registers (and immediate if i-type)
        #then convert to binary and write out to file
        fout.write() #FIXME
    elif args[0] == 'sw':
        #process registers (and immediate if i-type)
        #then convert to binary and write out to file
        fout.write() #FIXME
    elif args[0] == 'lw':
        #process registers (and immediate if i-type)
        #then convert to binary and write out to file
        fout.write() #FIXME
    elif args[0] == 'srl':
        #process registers (and immediate if i-type)
        #then convert to binary and write out to file
        fout.write() #FIXME
    elif args[0] == 'and':
        #process registers (and immediate if i-type)
        #then convert to binary and write out to file
        fout.write() #FIXME
    else:
        pass
