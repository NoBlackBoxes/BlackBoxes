CFILES = $(wildcard src/*.c)
OFILES = $(subst src,build/src,$(CFILES:.c=.o))
$(info CFILES is $(CFILES))
$(info OFILES is $(OFILES))
GCCFLAGS = -Wall -O2 -ffreestanding -nostdinc -nostdlib -nostartfiles
GCCPATH = _tmp/gcc-arm-10.3-2021.07-x86_64-aarch64-none-elf/bin

all: clean kernel8.img

build/src/boot.o: src/boot.S
	$(GCCPATH)/aarch64-none-elf-gcc $(GCCFLAGS) -c src/boot.S -o build/src/boot.o

build/%.o: %.c
	$(GCCPATH)/aarch64-none-elf-gcc $(GCCFLAGS) -c $< -o $@

kernel8.img: build/src/boot.o $(OFILES)
	$(GCCPATH)/aarch64-none-elf-ld -nostdlib build/src/boot.o $(OFILES) -T link.ld -o build/kernel8.elf
	$(GCCPATH)/aarch64-none-elf-objcopy -O binary build/kernel8.elf build/kernel8.img

clean:
	/bin/rm -rf build/*
	/bin/mkdir build/src
