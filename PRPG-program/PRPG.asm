addi $8, $0, 0xFFFF	#first register, seed value
addi $9, $0, 0x2000	#memory address register, will increment by 1
sw $8, ($9)		#store s0


#s1
mult $8, $8 	#square the seed 
mflo $8
andi $10, $8, 0xF	#bit mask the least significant (goes in r10, amd most significant (r18)
#lui, $1, 0xFFFF		#lui in this system will perform imm << 4 (not 16, as in MIPS)
#ori $1, $1, 0		
andi $18, $8, 0xF000
#and $18, $8, $1			
srl $18, $18, 8		# shift right by 8 bits the MSB's of the squared value stored in $18
or $8, $10, $18	# merge $17 and $18 to get the new 16-bit number, this is seed-i
addi $9, $9, 4	# increment address by one byte
sw $8 ($9)		# store this value in address stored in $14


#s2
mult $8, $8 	#square the seed 
mflo $8
andi $10, $8, 0xF	#bit mask the least significant (goes in r10, amd most significant (r18)
#lui, $1, 0xFFFF		#lui in this system will perform imm << 4 (not 16, as in MIPS)
#ori $1, $1, 0		
andi $18, $8, 0xF000
#and $18, $8, $1	
srl $18, $18, 8		# shift right by 8 bits the MSB's of the squared value stored in $18
or $8, $10, $18	# merge $17 and $18 to get the new 16-bit number, this is seed-i
addi $9, $9, 4	# increment address by one byte
sw $8 ($9)		# store this value in address stored in $14

#s3
mult $8, $8 	#square the seed 
mflo $8
andi $10, $8, 0xF	#bit mask the least significant (goes in r10, amd most significant (r18)
#lui, $1, 0xFFFF		#lui in this system will perform imm << 4 (not 16, as in MIPS)
#ori $1, $1, 0		
andi $18, $8, 0xF000
#and $18, $8, $1			
srl $18, $18, 8		# shift right by 8 bits the MSB's of the squared value stored in $18
or $8, $10, $18	# merge $17 and $18 to get the new 16-bit number, this is seed-i
addi $9, $9, 4	# increment address by one byte
sw $8 ($9)		# store this value in address stored in $14

#s4
mult $8, $8 	#square the seed 
mflo $8
andi $10, $8, 0xF	#bit mask the least significant (goes in r10, amd most significant (r18)
#lui, $1, 0xFFFF		#lui in this system will perform imm << 4 (not 16, as in MIPS)
#ori $1, $1, 0		
andi $18, $8, 0xF000
#and $18, $8, $1			
srl $18, $18, 8		# shift right by 8 bits the MSB's of the squared value stored in $18
or $8, $10, $18	# merge $17 and $18 to get the new 16-bit number, this is seed-i
addi $9, $9, 4	# increment address by one byte
sw $8 ($9)		# store this value in address stored in $14

#s5
mult $8, $8 	#square the seed 
mflo $8
andi $10, $8, 0xF	#bit mask the least significant (goes in r10, amd most significant (r18)
#lui, $1, 0xFFFF		#lui in this system will perform imm << 4 (not 16, as in MIPS)
#ori $1, $1, 0		
andi $18, $8, 0xF000
#and $18, $8, $1			
srl $18, $18, 8		# shift right by 8 bits the MSB's of the squared value stored in $18
or $8, $10, $18	# merge $17 and $18 to get the new 16-bit number, this is seed-i
addi $9, $9, 4	# increment address by one byte
sw $8 ($9)		# store this value in address stored in $14

#s6
mult $8, $8 	#square the seed 
mflo $8
andi $10, $8, 0xF	#bit mask the least significant (goes in r10, amd most significant (r18)
#lui, $1, 0xFFFF		#lui in this system will perform imm << 4 (not 16, as in MIPS)
#ori $1, $1, 0		
andi $18, $8, 0xF000
#and $18, $8, $1			
srl $18, $18, 8		# shift right by 8 bits the MSB's of the squared value stored in $18
or $8, $10, $18	# merge $17 and $18 to get the new 16-bit number, this is seed-i
addi $9, $9, 4	# increment address by one byte
sw $8 ($9)		# store this value in address stored in $14

#s7
mult $8, $8 	#square the seed 
mflo $8
andi $10, $8, 0xF	#bit mask the least significant (goes in r10, amd most significant (r18)
#lui, $1, 0xFFFF		#lui in this system will perform imm << 4 (not 16, as in MIPS)
#ori $1, $1, 0		
andi $18, $8, 0xF000
#and $18, $8, $1			
srl $18, $18, 8		# shift right by 8 bits the MSB's of the squared value stored in $18
or $8, $10, $18	# merge $17 and $18 to get the new 16-bit number, this is seed-i
addi $9, $9, 4	# increment address by one byte
sw $8 ($9)		# store this value in address stored in $14

#s8
mult $8, $8 	#square the seed 
mflo $8
andi $10, $8, 0xF	#bit mask the least significant (goes in r10, amd most significant (r18)
#lui, $1, 0xFFFF		#lui in this system will perform imm << 4 (not 16, as in MIPS)
#ori $1, $1, 0		
andi $18, $8, 0xF000
#and $18, $8, $1			
srl $18, $18, 8		# shift right by 8 bits the MSB's of the squared value stored in $18
or $8, $10, $18	# merge $17 and $18 to get the new 16-bit number, this is seed-i
addi $9, $9, 4	# increment address by one byte
sw $8 ($9)		# store this value in address stored in $14

#s9
mult $8, $8 	#square the seed 
mflo $8
andi $10, $8, 0xF	#bit mask the least significant (goes in r10, amd most significant (r18)
#lui, $1, 0xFFFF		#lui in this system will perform imm << 4 (not 16, as in MIPS)
#ori $1, $1, 0		
andi $18, $8, 0xF000
#and $18, $8, $1			
srl $18, $18, 8		# shift right by 8 bits the MSB's of the squared value stored in $18
or $8, $10, $18	# merge $17 and $18 to get the new 16-bit number, this is seed-i
addi $9, $9, 4	# increment address by one byte
sw $8 ($9)		# store this value in address stored in $14

#s10
mult $8, $8 	#square the seed 
mflo $8
andi $10, $8, 0xF	#bit mask the least significant (goes in r10, amd most significant (r18)
#lui, $1, 0xFFFF		#lui in this system will perform imm << 4 (not 16, as in MIPS)
#ori $1, $1, 0		
andi $18, $8, 0xF000
#and $18, $8, $1			
srl $18, $18, 8		# shift right by 8 bits the MSB's of the squared value stored in $18
or $8, $10, $18	# merge $17 and $18 to get the new 16-bit number, this is seed-i
addi $9, $9, 4	# increment address by one byte
sw $8 ($9)		# store this value in address stored in $14

#s11
mult $8, $8 	#square the seed 
mflo $8
andi $10, $8, 0xF	#bit mask the least significant (goes in r10, amd most significant (r18)
#lui, $1, 0xFFFF		#lui in this system will perform imm << 4 (not 16, as in MIPS)
#ori $1, $1, 0		
andi $18, $8, 0xF000
#and $18, $8, $1			
srl $18, $18, 8		# shift right by 8 bits the MSB's of the squared value stored in $18
or $8, $10, $18	# merge $17 and $18 to get the new 16-bit number, this is seed-i
addi $9, $9, 4	# increment address by one byte
sw $8 ($9)		# store this value in address stored in $14

#s12
mult $8, $8 	#square the seed 
mflo $8
andi $10, $8, 0xF	#bit mask the least significant (goes in r10, amd most significant (r18)
#lui, $1, 0xFFFF		#lui in this system will perform imm << 4 (not 16, as in MIPS)
#ori $1, $1, 0		
andi $18, $8, 0xF000
#and $18, $8, $1			
srl $18, $18, 8		# shift right by 8 bits the MSB's of the squared value stored in $18
or $8, $10, $18	# merge $17 and $18 to get the new 16-bit number, this is seed-i
addi $9, $9, 4	# increment address by one byte
sw $8 ($9)		# store this value in address stored in $14

#s13
mult $8, $8 	#square the seed 
mflo $8
andi $10, $8, 0xF	#bit mask the least significant (goes in r10, amd most significant (r18)
#lui, $1, 0xFFFF		#lui in this system will perform imm << 4 (not 16, as in MIPS)
#ori $1, $1, 0		
andi $18, $8, 0xF000
#and $18, $8, $1			
srl $18, $18, 8		# shift right by 8 bits the MSB's of the squared value stored in $18
or $8, $10, $18	# merge $17 and $18 to get the new 16-bit number, this is seed-i
addi $9, $9, 4	# increment address by one byte
sw $8 ($9)		# store this value in address stored in $14

#s14
mult $8, $8 	#square the seed 
mflo $8
andi $10, $8, 0xF	#bit mask the least significant (goes in r10, amd most significant (r18)
#lui, $1, 0xFFFF		#lui in this system will perform imm << 4 (not 16, as in MIPS)
#ori $1, $1, 0		
andi $18, $8, 0xF000
#and $18, $8, $1			
srl $18, $18, 8		# shift right by 8 bits the MSB's of the squared value stored in $18
or $8, $10, $18	# merge $17 and $18 to get the new 16-bit number, this is seed-i
addi $9, $9, 4	# increment address by one byte
sw $8 ($9)		# store this value in address stored in $14

#s15
mult $8, $8 	#square the seed 
mflo $8
andi $10, $8, 0xF	#bit mask the least significant (goes in r10, amd most significant (r18)
#lui, $1, 0xFFFF		#lui in this system will perform imm << 4 (not 16, as in MIPS)
#ori $1, $1, 0		
andi $18, $8, 0xF000
#and $18, $8, $1			
srl $18, $18, 8		# shift right by 8 bits the MSB's of the squared value stored in $18
or $8, $10, $18	# merge $17 and $18 to get the new 16-bit number, this is seed-i
addi $9, $9, 4	# increment address by one byte
sw $8 ($9)		# store this value in address stored in $14


#average value
subi $9, $9, 4	
lw $10 ($9)
add $8, $10, $8
subi $9, $9, 4
lw $10 ($9)
add $8, $10, $8
subi $9, $9, 4
lw $10 ($9)
add $8, $10, $8
subi $9, $9, 4
lw $10 ($9)
add $8, $10, $8
subi $9, $9, 4
lw $10 ($9)
add $8, $10, $8
subi $9, $9, 4
lw $10 ($9)
add $8, $10, $8
subi $9, $9, 4
lw $10 ($9)
add $8, $10, $8
subi $9, $9, 4
lw $10 ($9)
add $8, $10, $8
subi $9, $9, 4
lw $10 ($9)
add $8, $10, $8
subi $9, $9, 4
lw $10 ($9)
add $8, $10, $8
subi $9, $9, 4
lw $10 ($9)
add $8, $10, $8
subi $9, $9, 4
lw $10 ($9)
add $8, $10, $8
subi $9, $9, 4
lw $10 ($9)
add $8, $10, $8
subi $9, $9, 4
lw $10 ($9)
add $8, $10, $8
subi $9, $9, 4
lw $10 ($9)
add $8, $10, $8
#average
srl $8, $8, 4
addi $9, $9, 0x40
sw $8 ($9)
subi $9, $9, 0x40


#hamming weight, memory address is back at start
#s0
lw $8 ($9)	
addi $10, $0, 0
andi $8, $8, 1	#check bit 0
add $10, $10,$8
lw $8 ($9)
srl $8, $8, 1
andi $8, $8, 1 #check bit 1
add $10, $10,$8
lw $8 ($9)
srl $8, $8, 2
andi $8, $8, 1 #check bit 2
add $10, $10,$8
lw $8 ($9)
srl $8, $8, 3
andi $8, $8, 1 #check bit 3
add $10, $10,$8
lw $8 ($9)
srl $8, $8, 4
andi $8, $8, 1 #check bit 4
add $10, $10,$8
lw $8 ($9)
srl $8, $8, 5
andi $8, $8, 1 #check bit 5
add $10, $10,$8
lw $8 ($9)
srl $8, $8, 6
andi $8, $8, 1 #check bit 6
add $10, $10,$8
lw $8 ($9)
srl $8, $8, 7
andi $8, $8, 1 #check bit 7
add $10, $10,$8

addi $9, $9, 0x44
sw $10 ($9)
subi $9, $9 0x44
addi $9, $9, 4

#s1
lw $8 ($9)	
addi $10, $0, 0
andi $8, $8, 1	#check bit 0
add $10, $10,$8
lw $8 ($9)
srl $8, $8, 1
andi $8, $8, 1 #check bit 1
add $10, $10,$8
lw $8 ($9)
srl $8, $8, 2
andi $8, $8, 1 #check bit 2
add $10, $10,$8
lw $8 ($9)
srl $8, $8, 3
andi $8, $8, 1 #check bit 3
add $10, $10,$8
lw $8 ($9)
srl $8, $8, 4
andi $8, $8, 1 #check bit 4
add $10, $10,$8
lw $8 ($9)
srl $8, $8, 5
andi $8, $8, 1 #check bit 5
add $10, $10,$8
lw $8 ($9)
srl $8, $8, 6
andi $8, $8, 1 #check bit 6
add $10, $10,$8
lw $8 ($9)
srl $8, $8, 7
andi $8, $8, 1 #check bit 7
add $10, $10,$8

addi $9, $9, 0x44
sw $10 ($9)
subi $9, $9 0x44
addi $9, $9, 4

#s2
lw $8 ($9)	
addi $10, $0, 0
andi $8, $8, 1	#check bit 0
add $10, $10,$8
lw $8 ($9)
srl $8, $8, 1
andi $8, $8, 1 #check bit 1
add $10, $10,$8
lw $8 ($9)
srl $8, $8, 2
andi $8, $8, 1 #check bit 2
add $10, $10,$8
lw $8 ($9)
srl $8, $8, 3
andi $8, $8, 1 #check bit 3
add $10, $10,$8
lw $8 ($9)
srl $8, $8, 4
andi $8, $8, 1 #check bit 4
add $10, $10,$8
lw $8 ($9)
srl $8, $8, 5
andi $8, $8, 1 #check bit 5
add $10, $10,$8
lw $8 ($9)
srl $8, $8, 6
andi $8, $8, 1 #check bit 6
add $10, $10,$8
lw $8 ($9)
srl $8, $8, 7
andi $8, $8, 1 #check bit 7
add $10, $10,$8

addi $9, $9, 0x44
sw $10 ($9)
subi $9, $9 0x44
addi $9, $9, 4

#s3
lw $8 ($9)	
addi $10, $0, 0
andi $8, $8, 1	#check bit 0
add $10, $10,$8
lw $8 ($9)
srl $8, $8, 1
andi $8, $8, 1 #check bit 1
add $10, $10,$8
lw $8 ($9)
srl $8, $8, 2
andi $8, $8, 1 #check bit 2
add $10, $10,$8
lw $8 ($9)
srl $8, $8, 3
andi $8, $8, 1 #check bit 3
add $10, $10,$8
lw $8 ($9)
srl $8, $8, 4
andi $8, $8, 1 #check bit 4
add $10, $10,$8
lw $8 ($9)
srl $8, $8, 5
andi $8, $8, 1 #check bit 5
add $10, $10,$8
lw $8 ($9)
srl $8, $8, 6
andi $8, $8, 1 #check bit 6
add $10, $10,$8
lw $8 ($9)
srl $8, $8, 7
andi $8, $8, 1 #check bit 7
add $10, $10,$8

addi $9, $9, 0x44
sw $10 ($9)
subi $9, $9 0x44
addi $9, $9, 4

#s4
lw $8 ($9)	
addi $10, $0, 0
andi $8, $8, 1	#check bit 0
add $10, $10,$8
lw $8 ($9)
srl $8, $8, 1
andi $8, $8, 1 #check bit 1
add $10, $10,$8
lw $8 ($9)
srl $8, $8, 2
andi $8, $8, 1 #check bit 2
add $10, $10,$8
lw $8 ($9)
srl $8, $8, 3
andi $8, $8, 1 #check bit 3
add $10, $10,$8
lw $8 ($9)
srl $8, $8, 4
andi $8, $8, 1 #check bit 4
add $10, $10,$8
lw $8 ($9)
srl $8, $8, 5
andi $8, $8, 1 #check bit 5
add $10, $10,$8
lw $8 ($9)
srl $8, $8, 6
andi $8, $8, 1 #check bit 6
add $10, $10,$8
lw $8 ($9)
srl $8, $8, 7
andi $8, $8, 1 #check bit 7
add $10, $10,$8

addi $9, $9, 0x44
sw $10 ($9)
subi $9, $9 0x44
addi $9, $9, 4

#s5
lw $8 ($9)	
addi $10, $0, 0
andi $8, $8, 1	#check bit 0
add $10, $10,$8
lw $8 ($9)
srl $8, $8, 1
andi $8, $8, 1 #check bit 1
add $10, $10,$8
lw $8 ($9)
srl $8, $8, 2
andi $8, $8, 1 #check bit 2
add $10, $10,$8
lw $8 ($9)
srl $8, $8, 3
andi $8, $8, 1 #check bit 3
add $10, $10,$8
lw $8 ($9)
srl $8, $8, 4
andi $8, $8, 1 #check bit 4
add $10, $10,$8
lw $8 ($9)
srl $8, $8, 5
andi $8, $8, 1 #check bit 5
add $10, $10,$8
lw $8 ($9)
srl $8, $8, 6
andi $8, $8, 1 #check bit 6
add $10, $10,$8
lw $8 ($9)
srl $8, $8, 7
andi $8, $8, 1 #check bit 7
add $10, $10,$8

addi $9, $9, 0x44
sw $10 ($9)
subi $9, $9 0x44
addi $9, $9, 4

#s6
lw $8 ($9)	
addi $10, $0, 0
andi $8, $8, 1	#check bit 0
add $10, $10,$8
lw $8 ($9)
srl $8, $8, 1
andi $8, $8, 1 #check bit 1
add $10, $10,$8
lw $8 ($9)
srl $8, $8, 2
andi $8, $8, 1 #check bit 2
add $10, $10,$8
lw $8 ($9)
srl $8, $8, 3
andi $8, $8, 1 #check bit 3
add $10, $10,$8
lw $8 ($9)
srl $8, $8, 4
andi $8, $8, 1 #check bit 4
add $10, $10,$8
lw $8 ($9)
srl $8, $8, 5
andi $8, $8, 1 #check bit 5
add $10, $10,$8
lw $8 ($9)
srl $8, $8, 6
andi $8, $8, 1 #check bit 6
add $10, $10,$8
lw $8 ($9)
srl $8, $8, 7
andi $8, $8, 1 #check bit 7
add $10, $10,$8

addi $9, $9, 0x44
sw $10 ($9)
subi $9, $9 0x44
addi $9, $9, 4

#s7
lw $8 ($9)	
addi $10, $0, 0
andi $8, $8, 1	#check bit 0
add $10, $10,$8
lw $8 ($9)
srl $8, $8, 1
andi $8, $8, 1 #check bit 1
add $10, $10,$8
lw $8 ($9)
srl $8, $8, 2
andi $8, $8, 1 #check bit 2
add $10, $10,$8
lw $8 ($9)
srl $8, $8, 3
andi $8, $8, 1 #check bit 3
add $10, $10,$8
lw $8 ($9)
srl $8, $8, 4
andi $8, $8, 1 #check bit 4
add $10, $10,$8
lw $8 ($9)
srl $8, $8, 5
andi $8, $8, 1 #check bit 5
add $10, $10,$8
lw $8 ($9)
srl $8, $8, 6
andi $8, $8, 1 #check bit 6
add $10, $10,$8
lw $8 ($9)
srl $8, $8, 7
andi $8, $8, 1 #check bit 7
add $10, $10,$8

addi $9, $9, 0x44
sw $10 ($9)
subi $9, $9 0x44
addi $9, $9, 4

#s8
lw $8 ($9)	
addi $10, $0, 0
andi $8, $8, 1	#check bit 0
add $10, $10,$8
lw $8 ($9)
srl $8, $8, 1
andi $8, $8, 1 #check bit 1
add $10, $10,$8
lw $8 ($9)
srl $8, $8, 2
andi $8, $8, 1 #check bit 2
add $10, $10,$8
lw $8 ($9)
srl $8, $8, 3
andi $8, $8, 1 #check bit 3
add $10, $10,$8
lw $8 ($9)
srl $8, $8, 4
andi $8, $8, 1 #check bit 4
add $10, $10,$8
lw $8 ($9)
srl $8, $8, 5
andi $8, $8, 1 #check bit 5
add $10, $10,$8
lw $8 ($9)
srl $8, $8, 6
andi $8, $8, 1 #check bit 6
add $10, $10,$8
lw $8 ($9)
srl $8, $8, 7
andi $8, $8, 1 #check bit 7
add $10, $10,$8

addi $9, $9, 0x44
sw $10 ($9)
subi $9, $9 0x44
addi $9, $9, 4

#s9
lw $8 ($9)	
addi $10, $0, 0
andi $8, $8, 1	#check bit 0
add $10, $10,$8
lw $8 ($9)
srl $8, $8, 1
andi $8, $8, 1 #check bit 1
add $10, $10,$8
lw $8 ($9)
srl $8, $8, 2
andi $8, $8, 1 #check bit 2
add $10, $10,$8
lw $8 ($9)
srl $8, $8, 3
andi $8, $8, 1 #check bit 3
add $10, $10,$8
lw $8 ($9)
srl $8, $8, 4
andi $8, $8, 1 #check bit 4
add $10, $10,$8
lw $8 ($9)
srl $8, $8, 5
andi $8, $8, 1 #check bit 5
add $10, $10,$8
lw $8 ($9)
srl $8, $8, 6
andi $8, $8, 1 #check bit 6
add $10, $10,$8
lw $8 ($9)
srl $8, $8, 7
andi $8, $8, 1 #check bit 7
add $10, $10,$8

addi $9, $9, 0x44
sw $10 ($9)
subi $9, $9 0x44
addi $9, $9, 4

#s9
lw $8 ($9)	
addi $10, $0, 0
andi $8, $8, 1	#check bit 0
add $10, $10,$8
lw $8 ($9)
srl $8, $8, 1
andi $8, $8, 1 #check bit 1
add $10, $10,$8
lw $8 ($9)
srl $8, $8, 2
andi $8, $8, 1 #check bit 2
add $10, $10,$8
lw $8 ($9)
srl $8, $8, 3
andi $8, $8, 1 #check bit 3
add $10, $10,$8
lw $8 ($9)
srl $8, $8, 4
andi $8, $8, 1 #check bit 4
add $10, $10,$8
lw $8 ($9)
srl $8, $8, 5
andi $8, $8, 1 #check bit 5
add $10, $10,$8
lw $8 ($9)
srl $8, $8, 6
andi $8, $8, 1 #check bit 6
add $10, $10,$8
lw $8 ($9)
srl $8, $8, 7
andi $8, $8, 1 #check bit 7
add $10, $10,$8

addi $9, $9, 0x44
sw $10 ($9)
subi $9, $9 0x44
addi $9, $9, 4

#s10
lw $8 ($9)	
addi $10, $0, 0
andi $8, $8, 1	#check bit 0
add $10, $10,$8
lw $8 ($9)
srl $8, $8, 1
andi $8, $8, 1 #check bit 1
add $10, $10,$8
lw $8 ($9)
srl $8, $8, 2
andi $8, $8, 1 #check bit 2
add $10, $10,$8
lw $8 ($9)
srl $8, $8, 3
andi $8, $8, 1 #check bit 3
add $10, $10,$8
lw $8 ($9)
srl $8, $8, 4
andi $8, $8, 1 #check bit 4
add $10, $10,$8
lw $8 ($9)
srl $8, $8, 5
andi $8, $8, 1 #check bit 5
add $10, $10,$8
lw $8 ($9)
srl $8, $8, 6
andi $8, $8, 1 #check bit 6
add $10, $10,$8
lw $8 ($9)
srl $8, $8, 7
andi $8, $8, 1 #check bit 7
add $10, $10,$8

addi $9, $9, 0x44
sw $10 ($9)
subi $9, $9 0x44
addi $9, $9, 4

#s11
lw $8 ($9)	
addi $10, $0, 0
andi $8, $8, 1	#check bit 0
add $10, $10,$8
lw $8 ($9)
srl $8, $8, 1
andi $8, $8, 1 #check bit 1
add $10, $10,$8
lw $8 ($9)
srl $8, $8, 2
andi $8, $8, 1 #check bit 2
add $10, $10,$8
lw $8 ($9)
srl $8, $8, 3
andi $8, $8, 1 #check bit 3
add $10, $10,$8
lw $8 ($9)
srl $8, $8, 4
andi $8, $8, 1 #check bit 4
add $10, $10,$8
lw $8 ($9)
srl $8, $8, 5
andi $8, $8, 1 #check bit 5
add $10, $10,$8
lw $8 ($9)
srl $8, $8, 6
andi $8, $8, 1 #check bit 6
add $10, $10,$8
lw $8 ($9)
srl $8, $8, 7
andi $8, $8, 1 #check bit 7
add $10, $10,$8

addi $9, $9, 0x44
sw $10 ($9)
subi $9, $9 0x44
addi $9, $9, 4

#s12
lw $8 ($9)	
addi $10, $0, 0
andi $8, $8, 1	#check bit 0
add $10, $10,$8
lw $8 ($9)
srl $8, $8, 1
andi $8, $8, 1 #check bit 1
add $10, $10,$8
lw $8 ($9)
srl $8, $8, 2
andi $8, $8, 1 #check bit 2
add $10, $10,$8
lw $8 ($9)
srl $8, $8, 3
andi $8, $8, 1 #check bit 3
add $10, $10,$8
lw $8 ($9)
srl $8, $8, 4
andi $8, $8, 1 #check bit 4
add $10, $10,$8
lw $8 ($9)
srl $8, $8, 5
andi $8, $8, 1 #check bit 5
add $10, $10,$8
lw $8 ($9)
srl $8, $8, 6
andi $8, $8, 1 #check bit 6
add $10, $10,$8
lw $8 ($9)
srl $8, $8, 7
andi $8, $8, 1 #check bit 7
add $10, $10,$8

addi $9, $9, 0x44
sw $10 ($9)
subi $9, $9 0x44
addi $9, $9, 4

#s13
lw $8 ($9)	
addi $10, $0, 0
andi $8, $8, 1	#check bit 0
add $10, $10,$8
lw $8 ($9)
srl $8, $8, 1
andi $8, $8, 1 #check bit 1
add $10, $10,$8
lw $8 ($9)
srl $8, $8, 2
andi $8, $8, 1 #check bit 2
add $10, $10,$8
lw $8 ($9)
srl $8, $8, 3
andi $8, $8, 1 #check bit 3
add $10, $10,$8
lw $8 ($9)
srl $8, $8, 4
andi $8, $8, 1 #check bit 4
add $10, $10,$8
lw $8 ($9)
srl $8, $8, 5
andi $8, $8, 1 #check bit 5
add $10, $10,$8
lw $8 ($9)
srl $8, $8, 6
andi $8, $8, 1 #check bit 6
add $10, $10,$8
lw $8 ($9)
srl $8, $8, 7
andi $8, $8, 1 #check bit 7
add $10, $10,$8

addi $9, $9, 0x44
sw $10 ($9)
subi $9, $9 0x44
addi $9, $9, 4

#s14
lw $8 ($9)	
addi $10, $0, 0
andi $8, $8, 1	#check bit 0
add $10, $10,$8
lw $8 ($9)
srl $8, $8, 1
andi $8, $8, 1 #check bit 1
add $10, $10,$8
lw $8 ($9)
srl $8, $8, 2
andi $8, $8, 1 #check bit 2
add $10, $10,$8
lw $8 ($9)
srl $8, $8, 3
andi $8, $8, 1 #check bit 3
add $10, $10,$8
lw $8 ($9)
srl $8, $8, 4
andi $8, $8, 1 #check bit 4
add $10, $10,$8
lw $8 ($9)
srl $8, $8, 5
andi $8, $8, 1 #check bit 5
add $10, $10,$8
lw $8 ($9)
srl $8, $8, 6
andi $8, $8, 1 #check bit 6
add $10, $10,$8
lw $8 ($9)
srl $8, $8, 7
andi $8, $8, 1 #check bit 7
add $10, $10,$8

addi $9, $9, 0x44
sw $10 ($9)
subi $9, $9 0x4

lw $8 ($9)
add $10, $10, $8 #s15 ham + s14 ham
subi $9, $9, 4
lw $8 ($9)
add $10, $10, $8
subi $9, $9, 4
lw $8 ($9)
add $10, $10, $8
subi $9, $9, 4
lw $8 ($9)
add $10, $10, $8
subi $9, $9, 4
lw $8 ($9)
add $10, $10, $8
subi $9, $9, 4
lw $8 ($9)
add $10, $10, $8
subi $9, $9, 4
lw $8 ($9)
add $10, $10, $8
subi $9, $9, 4
lw $8 ($9)
add $10, $10, $8
subi $9, $9, 4
lw $8 ($9)
add $10, $10, $8
subi $9, $9, 4
lw $8 ($9)
add $10, $10, $8
subi $9, $9, 4
lw $8 ($9)
add $10, $10, $8
subi $9, $9, 4
lw $8 ($9)
add $10, $10, $8
subi $9, $9, 4
lw $8 ($9)
add $10, $10, $8
subi $9, $9, 4
lw $8 ($9)
add $10, $10, $8
subi $9, $9, 4
lw $8 ($9)
add $10, $10, $8
subi $9, $9, 4


#average
srl $10, $10, 4
addi $9, $9, 0x44
sw $10 ($9)

