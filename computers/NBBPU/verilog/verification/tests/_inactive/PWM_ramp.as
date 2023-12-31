SEL 0 F 2   #00 Set lower byte of reg 2 to FF
SEU 0 0 2   #01 Set upper byte of reg 2 to 00
SEL 0 1 3   #02 Set lower byte of reg 3 to 01
SEU 0 0 3   #03 Set upper byte of reg 3 to 00
SEL 0 6 4   #04 Set lower byte of reg 4 to 06
SEU 0 0 4   #05 Set upper byte of reg 4 to 00
SUB 2 3 2   #06 Subtract values (regs 2 - 3), store result in reg 2
SEL 0 0 5   #pwm Set lower byte of reg 5 to 00
SEU 8 0 5   #pwm Set upper byte of reg 5 to 80
STR 5 2 0   #pwm Store value in reg 2 at address in reg 5
BRN 4 2 0   #07 Branch to reg 4 if reg 2 != 0
SEL F 0 2   #xx Set lower byte of reg 2 to F0
SEU F F 2   #xx Set upper byte of reg 2 to FF
SEL 2 A 3   #xx Set lower byte of reg 3 to 2A (d42)
SEU 0 0 3   #xx Set upper byte of reg 3 to 00
STR 2 3 0   #xx Store value in reg 3 at address in reg 2
#FIN