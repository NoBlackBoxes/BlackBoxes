.globl PUT32
PUT32:
	str w1,[x0]
	ret

.globl GET32
GET32:
	ldr w0,[x0]
	ret

.globl TICK
TICK:
	subs x0, x0, #1
	bne TICK
	ret