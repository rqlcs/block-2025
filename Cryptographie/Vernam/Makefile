CC = gcc
CFLAGS = -ansi -Wall
EXE = vernam
OFILES = vernam.o codage.o decodage.o key.o
but : ${EXE}

${EXE}: ${OFILES}
	$(CC) $(CFLAGS) -o ${EXE} ${OFILES}
  
mrproper : clean but

.PHONY : but clean mrproper 

clean :	$(OFILES)
	rm -f $(OFILES)
