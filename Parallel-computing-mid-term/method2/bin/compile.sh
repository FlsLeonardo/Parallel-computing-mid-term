#!/bin/bash

if [ $# -eq 0 ]; then
  module load gcc91
  g++-9.1.0 -c main.cpp -fopenmp
  g++-9.1.0 -c serialTransposition.cpp
  g++-9.1.0 -c implicitTransposition.cpp -O1
  g++-9.1.0 -c ompTransposition.cpp -fopenmp
  g++-9.1.0 main.o serialTransposition.o implicitTransposition.o ompTransposition.o -o Main -fopenmp
  ./Main 4 "O1"
  ./Main 5 "O1"
  ./Main 6 "O1"
  ./Main 7 "O1"
  ./Main 8 "O1"
  ./Main 9 "O1"
  ./Main 10 "O1"
  ./Main 11 "O1"
  ./Main 12 "O1"
  
  
  g++-9.1.0 -c main.cpp -fopenmp
  g++-9.1.0 -c serialTransposition.cpp
  g++-9.1.0 -c implicitTransposition.cpp -O2
  g++-9.1.0 -c ompTransposition.cpp -fopenmp
  g++-9.1.0 main.o serialTransposition.o implicitTransposition.o ompTransposition.o -o Main -fopenmp
  ./Main 4 "O2"
  ./Main 5 "O2"
  ./Main 6 "O2"
  ./Main 7 "O2"
  ./Main 8 "O2"
  ./Main 9 "O2"
  ./Main 10 "O2"
  ./Main 11 "O2"
  ./Main 12 "O2"
  
  rm ../output/Serial.csv
  rm ../output/Omp.csv
  g++-9.1.0 -c main.cpp -fopenmp
  g++-9.1.0 -c serialTransposition.cpp
  g++-9.1.0 -c implicitTransposition.cpp -O3 
  g++-9.1.0 -c ompTransposition.cpp -fopenmp
  g++-9.1.0 main.o serialTransposition.o implicitTransposition.o ompTransposition.o -o Main -fopenmp
  ./Main 4 "O3"
  ./Main 5 "O3"
  ./Main 6 "O3"
  ./Main 7 "O3"
  ./Main 8 "O3"
  ./Main 9 "O3"
  ./Main 10 "O3"
  ./Main 11 "O3"
  ./Main 12 "O3"
fi

if [ $# -eq 1 ]; then
    module load gcc91
    g++-9.1.0 -c main.cpp -fopenmp
    g++-9.1.0 -c serialTransposition.cpp
    g++-9.1.0 -c implicitTransposition.cpp -$1
    g++-9.1.0 -c ompTransposition.cpp -fopenmp
    g++-9.1.0 main.o serialTransposition.o implicitTransposition.o ompTransposition.o -o Main -fopenmp
    echo $1
   ./Main 4 $1
   ./Main 5 $1
   ./Main 6 $1
   ./Main 7 $1
   ./Main 8 $1
   ./Main 9 $1
   ./Main 10 $1
   ./Main 11 $1
   ./Main 12 $1
fi



if [ $# -eq 2 ]; then
  # Compilazione dei file
  module load gcc91
  g++-9.1.0 -c main.cpp -fopenmp
  g++-9.1.0 -c serialTransposition.cpp
  g++-9.1.0 -c implicitTransposition.cpp -$1
  g++-9.1.0 -c ompTransposition.cpp -fopenmp
  
  # Link dei file oggetto
  g++-9.1.0 main.o serialTransposition.o implicitTransposition.o ompTransposition.o -o Main -fopenmp
  # Eseguiamo il programma col parametro
  ./Main $2 $1
fi