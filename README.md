# ECE* 366* G9* Proj3
Project 3 for ECE 366, group 9 repo

Requirements:

for the language:
* 8bit instructions and 8bit data
* we can create whatever instructions we want/need for running our PRPG
* come up with encoding scheme -  in progress (vishal)
* decide on register/memory usage -  done (sammi)
* for a single cycle CPU

for the hardware design:
* internal ALU diagram showing how instructions get implemented -  done (JB)
* CPU diagram supporting the single cycle instructions -  is this done?

#Instructions used in PRPG (UPDATED)
note that immediates/constant will need 4 bits
* half_lui
* addi_r0
* sw
* mult
* mask_top
* andi_r3
* srl
* or_r
* addi_r1
* branch_nz
* count_reset
* lw
* add_r
* sub_count
* subi_r1
* zero

To turn in:

* instruction table showing controls for single cycle -  in progress (vishal)
* CPU diagram -  same as the class examples or?
* ALU diagram -  final look?
* machine code source file for PRPG -  done, just need opcodes (sammi)
* python source code for simulator -  in progress (sammi, after )
* report -  TODO (everyone)
