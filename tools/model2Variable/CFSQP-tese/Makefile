ARCH=$(shell uname -m)


ifeq ($(ARCH),armv6l)
	C = armv6l-unknown-linux-gnueabihf-gcc
	CFLAGS= -march=armv6z -mtune=arm1176jzf-s -mfpu=vfp -mfloat-abi=hard
	#CFLAGS= -mfloat-abi=hard -mfpu=vfp -march=native  -mcpu=arm1176jzf-s -O2
	RAN = armv6l-unknown-linux-gnueabihf-gcc-ranlib
else
	C=gcc
	CFLAGS = -O3
	RAN = ranlib
endif

AR= ar
LINUX= -lrt	


MyLibs = ~/myLibs/
MyIncludes= ~/myIncludes/
XMLLIB=`xml2-config --cflags --libs`

all:robotControl

LIBDATAHANDLE:
	$(C) $(CFLAGS) -c $(XMLLIB)  dataHandler.c
	$(AR) rs libDataHandle.a dataHandler.o

robotControl:LIBDATAHANDLE
	$(C) $(CFLAGS) -c qld.c -I. -L.
	$(C) $(CFLAGS) -c cfsqp.c -I. -L.
	$(C) $(CFLAGS) -c $(XMLLIB) -I. -L. -o RobotControl.o RobotControl.c   ./libDataHandle.a 
	$(C) $(XMLLIB) -I. -L. qld.o cfsqp.o RobotControl.o   ./libDataHandle.a -o teste.o -lm
		 

robotControlDebug:LIBDATAHANDLE
	$(C) $(CFLAGS) -c -g3  qld.c -I. -L.
	$(C) $(CFLAGS) -c -g3 cfsqp.c -I. -L.
	$(C) -c $(XMLLIB) -g3 -I. -L. -o Robotcontrol.o RobotControl.c -lrt  ./libDataHandle.a
	$(C) $(XMLLIB) -I.  -g3 -L. qld.o cfsqp.o Robotcontrol.o -lrt ./libDataHandle.a -o teste.o -lm

.c.o: 
	$(CC) $(CFLAGS) -c qld.c
	$(CC) $(CFLAGS) -c cfsqp.c
 
libcfsqp.a: qld.o cfsqp.o 
	$(AR) cr libcfsqp.a $?
	$(RAN) libcfsqp.a 

clean:
	'pwd'
	`rm *.o *.a`
