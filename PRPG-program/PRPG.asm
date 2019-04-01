addi $8, $0, 199	#first register, seed value
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
