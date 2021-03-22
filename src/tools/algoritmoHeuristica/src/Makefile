ARCH=uname -m

ifeq ($ARCH,armv6l)
        C = armv6l-unknown-linux-gnueabihf-gcc
        CFLAGS= -mfloat-abi=hard -mfpu=vfp -march=native  -mcpu=arm1176jzf-s -O2  -lcblas -latlas -lm
        RAN = armv6l-unknown-linux-gnueabihf-gcc-ranlib
else
        C=g++
        CFLAGS = -O3
endif

LINUX= -lrt -O3


all:HEURIS HEURISD 


HEURIS:
	$(C) $(LINUX)  main.cpp RegraDeOrdenacao.cpp task.cpp  Tripla.cpp subgradiente.cpp -o alg.o


HEURISD:
	$(C) -g3  $(LINUX)  main.cpp RegraDeOrdenacao.cpp task.cpp  Tripla.cpp subgradiente.cpp -o algd.o 

clean:
	'pwd'
	`rm *.o *.a`
