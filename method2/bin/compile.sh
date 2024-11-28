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
  
fi

# Se viene passato un solo parametro (O1, O2, etc.)
if [ $# -eq 1 ]; then
    module load gcc91
    g++-9.1.0 -c main.cpp -fopenmp
    g++-9.1.0 -c serialTransposition.cpp
    
    # Se il parametro contiene uno spazio, lo dividiamo nei flag
    OPTS=($1)  # Usa un array per gestire i flag separati
    
    # Compilazione con i flag separati
    g++-9.1.0 -c implicitTransposition.cpp -"${OPTS[@]}"  # Passa i flag separati
    g++-9.1.0 -c ompTransposition.cpp -fopenmp
    g++-9.1.0 main.o serialTransposition.o implicitTransposition.o ompTransposition.o -o Main -fopenmp
    
    echo "Compilazione con i seguenti flag: ${OPTS[@]}"  # Mostra i flag usati
    
    # Passiamo la stringa completa (concatenata) al programma Main
    FLAGS="$1"  # La stringa passata da concatenare
    ./Main 4 "$FLAGS"
    ./Main 5 "$FLAGS"
    ./Main 6 "$FLAGS"
    ./Main 7 "$FLAGS"
    ./Main 8 "$FLAGS"
    ./Main 9 "$FLAGS"
    ./Main 10 "$FLAGS"
    ./Main 11 "$FLAGS"
    ./Main 12 "$FLAGS"
fi

# Se vengono passati due parametri
if [ $# -eq 2 ]; then
  # Compilazione dei file
  module load gcc91
  g++-9.1.0 -c main.cpp -fopenmp
  g++-9.1.0 -c serialTransposition.cpp
  
  OPTS=($1)  # Usa un array per gestire i flag separati
  g++-9.1.0 -c implicitTransposition.cpp -"${OPTS[@]}"  # Passa i flag separati
  g++-9.1.0 -c ompTransposition.cpp -fopenmp
  
  # Link dei file oggetto
  g++-9.1.0 main.o serialTransposition.o implicitTransposition.o ompTransposition.o -o Main -fopenmp
  # Eseguiamo il programma col parametro
  FLAGS="$1"  # La stringa passata da concatenare
  ./Main $2 "$FLAGS"  # Passa i flag concatenati al programma Main
fi
