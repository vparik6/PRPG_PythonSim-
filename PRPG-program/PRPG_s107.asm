#the initial seed code goes here, will be different for each seed
half_lui 6       # has implicit register use, r3 = x << 4
addi_r0 11	       # r0 = 15
or_r 3 0       # 3 is register destination, or of r3 r0

#store s0
sw 3 1  #contents of r3 stored at address in r1
mult 3 3	       #square the seed
mask_top 2 3     #stores mask of most significant 3 bits of r3 in r2
andi_r3 15	       #bit mask the least significant 3 bits of r3, store in r3
srl 2 1		       # r2 = r2 >> 8
or_r 3 2        	 # r3 = r3 or r2
addi_r1 1	       # r1 = r1 + 1  memory address increment
sub_count 1         #decriment counter register by 1
sw 3 1
branch_nz 7         #if implicit counter register != 0, pc -= r7
count_reset

#seed sum
subi_r1 1
lw 2 1
add_r 3 2
sub_count 1
branch_nz 9

#average
addi_r1 1
srl 3 2
addi_r1 15
addi_r1 1
sw 3 1
subi_r1 15
subi_r1 1     #memory address in r1 back at 2008
count_reset

#hamming weight, memory address is back at start
lw 3 1
zero 2      #r2 = 0 (number of set bits counter)
andi_r3 1	#check bit 0
add_r 2 3   #r2 = r2 + r3
lw 3 1    #reload value at address in r1
srl 3 0
andi_r3 1 #check bit 1
add_r 2 3   #r2 = r2 + r3
lw 3 1
srl 3 0
srl 3 0
andi_r3 1 #check bit 2
add_r 2 3   #r2 = r2 + r3
lw 3 1
srl 3 0
srl 3 0
srl 3 0
andi_r3 1 #check bit 3
add_r 2 3   #r2 = r2 + r3
lw 3 1
srl 3 0
srl 3 0
srl 3 0
srl 3 0
andi_r3 1 #check bit 4
add_r 2 3   #r2 = r2 + r3
lw 3 1
srl 3 0
srl 3 0
srl 3 0
srl 3 0
srl 3 0
andi_r3 1 #check bit 5
add_r 2 3   #r2 = r2 + r3
lw 3 1
srl 3 0
srl 3 0
srl 3 0
srl 3 0
srl 3 0
srl 3 0
andi_r3 1 #check bit 6
add_r 2 3   #r2 = r2 + r3
lw 3 1
srl 3 0
srl 3 0
srl 3 0
srl 3 0
srl 3 0
srl 3 0
srl 3 0
andi_r3 1 #check bit 7
add_r 2 3   #r2 = r2 + r3
addi_r1 15
addi_r1 3   #move forward 18 bytes in memory
sw 2 1      #store r2 in that address
subi_r1 15
subi_r1 2   #memory update to next seed value, requires subtraction by 16
sub_count 1
branch_nz 8   #if implicit counter register != 0, pc -= r8
count_reset
addi_r1 1     # address should now be M[18]
lw 2 1        #load h0 to r2

#hamming sum
addi_r1 1     # address of next hamming number
lw 3 1        #load to temp
add_r 2 3       #add_r to total sum
sub_count 1   #decrement counter
branch_nz 10   #if counter != 0, loop

#average
srl 2 2       #r2 = r2 >> 4
sw 2 1        #store r2 in address in r1
