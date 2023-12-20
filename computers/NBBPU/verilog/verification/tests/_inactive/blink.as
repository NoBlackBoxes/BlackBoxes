SEL 0 4 6   #01 Set lower byte of reg 5 to 06 - Outer loop address (4)
SEU 0 0 6   #02 Set upper byte of reg 5 to 00 - 
SEL 0 A 4   #03 Set lower byte of reg 4 to 03 - Num Loops
SEU 0 0 4   #04 Set upper byte of reg 4 to 00 -
SEL F F 2   #05 Set lower byte of reg 2 to 10 - Loop limit
SEU F F 2   #06 Set upper byte of reg 2 to 00 - 
SEL 0 1 3   #07 Set lower byte of reg 3 to 01 - Loop step
SEU 0 0 3   #08 Set upper byte of reg 3 to 00 - 
SEL 0 A 5   #09 Set lower byte of reg 5 to 06 - Inner loop address
SEU 0 0 5   #10 Set upper byte of reg 5 to 00 - 
SUB 2 3 2   #11 Subtract values in regs 3 and 2, store result in reg 2
BRN 5 2 0   #12 Branch to reg 5 if reg 2 != 0
SUB 4 3 4   #13 Subtract values in regs 4 and 3, store result in reg 4
BRN 6 4 0   #14 Branch to reg 6 if reg 4 != 0
SEL 0 0 2   #15 Set lower byte of reg 2 to 00
SEU 0 0 2   #16 Set upper byte of reg 2 to 00
SEL 0 0 3   #17 Set lower byte of reg 3 to 00
SEU F 1 3   #18 Set upper byte of reg 3 to F0
STR 2 3 0   #19 Store value in reg 3 at address in reg 2
SEL 1 7 6   #20 Set lower byte of reg 5 to 06 - Outer loop address (23)
SEU 0 0 6   #21 Set upper byte of reg 5 to 00 - 
SEL 0 A 4   #22 Set lower byte of reg 4 to 03 - Num Loops
SEU 0 0 4   #23 Set upper byte of reg 4 to 00 -
SEL F F 2   #24 Set lower byte of reg 2 to 10 - Loop limit
SEU F F 2   #25 Set upper byte of reg 2 to 00 - 
SEL 0 1 3   #26 Set lower byte of reg 3 to 01 - Loop step
SEU 0 0 3   #27 Set upper byte of reg 3 to 00 - 
SEL 1 D 5   #28 Set lower byte of reg 5 to 06 - Inner loop address (29)
SEU 0 0 5   #29 Set upper byte of reg 5 to 00 - 
SUB 2 3 2   #30 Subtract values in regs 3 and 2, store result in reg 2
BRN 5 2 0   #31 Branch to reg 5 if reg 2 != 0
SUB 4 3 4   #32 Subtract values in regs 4 and 3, store result in reg 4
BRN 6 4 0   #33 Branch to reg 6 if reg 4 != 0
SEL 0 0 2   #34 Set lower byte of reg 2 to 00
SEU 0 0 2   #35 Set upper byte of reg 2 to 00
SEL 0 0 3   #36 Set lower byte of reg 3 to 00
SEU F 0 3   #37 Set upper byte of reg 3 to F0
STR 2 3 0   #38 Store value in reg 3 at address in reg 2
JMP 0 0 1   #39 Repeat
#FIN