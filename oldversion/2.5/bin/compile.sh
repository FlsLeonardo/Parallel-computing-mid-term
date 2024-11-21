#!/bin/bash

if [ $# -eq 0 ]; then
    echo "Usage: $0 <matrix_size>"
    exit 1
fi

# Compilazione dei file
module load gcc91
g++-9.1.0 -c main.cpp -fopenmp
g++-9.1.0 -c serialTransposition.cpp
g++-9.1.0 -c implicitTransposition.cpp -O1
g++-9.1.0 -c ompTransposition.cpp -fopenmp

# Link dei file oggetto
g++-9.1.0 main.o serialTransposition.o implicitTransposition.o ompTransposition.o -o Main -fopenmp

# Eseguiamo il programma 
./Main $1