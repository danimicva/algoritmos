CC=gcc
CFLAGS=-Wall -std=gnu99
SOURCES=main.c sort.c bubblesort.c mergesort.c insertionsort.c lista.c
SALIDA=salida.csv
EXECUTABLE=main

all:    
	$(CC)  $(CFLAGS) $(SOURCES) -o $(EXECUTABLE)

clean_part:
	rm -f *.o

clean:
	rm -f *.o $(EXECUTABLE) $(SALIDA)