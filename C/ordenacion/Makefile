CC=gcc
CFLAGS=-Wall
SOURCES=main.c sort.c bubblesort.c mergesort.c insertionsort.c lista.c
OBJECTS=$(SOURCES:.c=.o)
SALIDA=salida.csv
EXECUTABLE=sort

all: $(SOURCES) $(EXECUTABLE) clean_part
    
$(EXECUTABLE): $(OBJECTS) 
	$(CC) $(LDFLAGS) $(OBJECTS) -o $@

.o:
	$(CC) $(CFLAGS) $< -o $@

clean_part:
	rm -f *.o

clean:
	rm -f *.o $(EXECUTABLE) $(SALIDA)