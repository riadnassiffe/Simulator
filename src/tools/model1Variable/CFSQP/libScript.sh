#!/bin/sh

gcc -c -fpic  `xml2-config --cflags --libs` dataHandler.c 
gcc -shared -o libDataHandle.so dataHandler.o 
gcc -c `xml2-config --cflags --libs` dataHandler.c 
ar rs libDataHandle.a dataHandler.o 

