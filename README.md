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

#Instructions used in PRPG
note that immediates/constant will need 4 bits
* addi
* lui
* andi
* subi
* add
* mult
* sw
* lw
* srl
* and
* ori (I think we need this to go with lui for immediates greater than 4 bits, but it's possible maybe it can be special and have its own format, if need be?)


To turn in:

* instruction table showing controls for single cycle -  in progress (vishal)
* CPU diagram -  same as the class examples or?
* ALU diagram -  final look?
* machine code source file for PRPG -  TODO (sammi)
* python source code for simulator -  in progress (sammi, after )
* report -  TODO (everyone)
