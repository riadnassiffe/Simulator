#C=armv6l-unknown-linux-gnueabihf-gcc
#CFLAGS = mfloat-abi=hard -mfpu=vfp -march=native  -mcpu=arm1176jzf-s -O2  -lcblas -latlas -lm
#RAN = armv6l-unknown-linux-gnueabihf-gcc-ranlib
C=gcc
CFLAGS= -o3 -lm

MyLibs = ~/myLibs/
MyIncludes= ~/myIncludes/
XMLLIB=`xml2-config --cflags --libs`

CFLAGS = -O2

LIBDATAHANDLE:
	$(C) $(CFLAGS) -c $(XMLLIB)  dataHandler.c
	ar rs libDataHandle.a dataHandler.o

robotControl:LIBDATAHANDLE
	$(C) $(CFLAGS) -c qld.c -I. -L.
	$(C) $(CFLAGS) -c cfsqp.c -I. -L.
	$(C) $(CFLAGS) -c $(XMLLIB) -I. -L. -o RobotControl.o RobotControl.c   ./libDataHandle.a 
	$(C) $(XMLLIB) -I. -L. qld.o cfsqp.o RobotControl.o   ./libDataHandle.a -o teste.o -lm
	
robotControl2:
	$(C) $(CFLAGS) -c -Wall -fPIC -lcrypt  $(XMLLIB)  dataHandler.c
	gcc -shared -Wl,-soname,libDataHandle.so.1 -o libDataHandle.so dataHandler.o
	$(C) $(CFLAGS) -c  -shared -fpic -lcrypt  qld.c -I. -L.
	$(C) $(CFLAGS) -c  -shared -fpic -lcrypt cfsqp.c -I. -L.
	$(C) $(CFLAGS) $(XMLLIB) -I. -L.  qld.o cfsqp.o   RobotControl.c -lrt  ./libDataHandle.so -o RobotControl.o -lm
	 

robotControlDebug:LIBDATAHANDLE
	$(C) $(CFLAGS) -c -g3  qld.c -I. -L.
	$(C) $(CFLAGS) -c -g3 cfsqp.c -I. -L.
	$(C) -c $(XMLLIB) -g3 -I. -L. -o Robotcontrol.o RobotControl.c -lrt  ./libDataHandle.a
	$(C) $(XMLLIB) -I.  -g3 -L. qld.o cfsqp.o Robotcontrol.o -lrt ./libDataHandle.a -o testeD.o -lm

#roboSolver:LIBDATAHANDLE
#	$(C) $(CFLAGS) -c qld.c -I. -L.
#	$(C) $(CFLAGS) -c cfsqp.c -I. -L.
#	$(C) $(CFLAGS) -c $(XMLLIB) -I. -L. -o RoboSolver.o RoboSolver.c -lrt  ./libDataHandle.a 
#	ar -cvq libRoboSolver.a RoboSolver.o qld.o cfsqp.o 

#roboSolver2:
#	$(C) $(CFLAGS) -c -Wall -fPIC -lcrypt  $(XMLLIB)  dataHandler.c
#	gcc -shared -Wl,-soname,libDataHandle.so.1 -o libDataHandle.so dataHandler.o
#	$(C) $(CFLAGS) -c  -shared -fpic -lcrypt  qld.c -I. -L.
#	$(C) $(CFLAGS) -c  -shared -fpic -lcrypt cfsqp.c -I. -L.
#	$(C) $(CFLAGS) -c -shared -fpic -lcrypt $(XMLLIB) -I. -L. -o RoboSolver.o RoboSolver.c -lrt  ./libDataHandle.so
#	gcc -shared -Wl,-soname,libRoboSolver.so.1 -o libRoboSolver.so  qld.o cfsqp.o RoboSolver.o
#	

#LIBDATAHANDLEDEBUG:
#	$(C) -C $(XMLLIB) -g3 dataHandler.c	
#	ar rs libDataHandle.a dataHandler.o


.c.o: 
	$(CC) $(CFLAGS) -c qld.c
	$(CC) $(CFLAGS) -c cfsqp.c
 
libcfsqp.a: qld.o cfsqp.o 
	ar cr libcfsqp.a $?
	$(RAN) libcfsqp.a 

clean:
	rm *.a *.o
