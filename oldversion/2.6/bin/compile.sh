#!/bin/bash

# Compilazione dei file
module load gcc91
g++-9.1.0 -c main.cpp -fopenmp
g++-9.1.0 -c serialTransposition.cpp
g++-9.1.0 -c implicitTransposition.cpp -O3
g++-9.1.0 -c ompTransposition.cpp -fopenmp

# Link dei file oggetto
g++-9.1.0 main.o serialTransposition.o implicitTransposition.o ompTransposition.o -o Main -fopenmp

if [ $# -eq 0 ]; then
   ./Main 4
   ./Main 5
   ./Main 6
   ./Main 7
   ./Main 8
   ./Main 9
   ./Main 10
   ./Main 11
   ./Main 12
else
  # Eseguiamo il programma col parametro
  ./Main $1
fi