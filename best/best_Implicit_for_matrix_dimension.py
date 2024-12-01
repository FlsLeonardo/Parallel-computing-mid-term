import sys
import pandas as pd
import numpy as np
import csv
from collections import defaultdict

def main():
    # Controllo se sono stati forniti parametri
    if len(sys.argv) < 2:
        compare("../method1/output/Implicit.csv","../method2/output/Implicit.csv","../method3/output/Implicit.csv","best.csv")
        sys.exit(1)
    for arg in sys.argv:
        if "--help" in arg:
            print("\nHai richiesto l'aiuto.")
            print("-type=(serial, implicit, omp)")
            print("-ES=(number)")
            sys.exit(0)
    


def compare(file1, file2, file3, output_file):
    # Liste per memorizzare i dati dei tre file
    dim1, time1, impl1 = [], [], []
    dim2, time2, impl2 = [], [], []
    dim3, time3, impl3 = [], [], []
    
    # Funzione per leggere un file e popolare le liste
    def read_file(filename, dim_list, time_list, impl_list):
        with open(filename, mode='r') as file:
            reader = csv.reader(file, delimiter=';')
            for row in reader:
                dim_list.append(int(row[0]))  # Prima colonna: Dimensione
                time_list.append(float(row[1]))  # Seconda colonna: Tempo
                impl_list.append(row[2])  # Terza colonna: Implementazione

    # Leggi i tre file nei rispettivi gruppi di liste
    read_file(file1, dim1, time1, impl1)
    read_file(file2, dim2, time2, impl2)
    read_file(file3, dim3, time3, impl3)

    # Combina i dati in un'unica lista complessiva
    combined_dims = dim1 + dim2 + dim3
    combined_times = time1 + time2 + time3
    combined_impls = impl1 + impl2 + impl3

    # Calcola le medie dei tempi per ciascuna combinazione di dimensione e implementazione
    unique_keys = {}  # Dizionario per tenere traccia delle somme e dei conteggi
    for dim, time, impl in zip(combined_dims, combined_times, combined_impls):
        key = (dim, impl)  # Chiave unica: (dimensione, implementazione)
        if key not in unique_keys:
            unique_keys[key] = {'sum': 0, 'count': 0}
        unique_keys[key]['sum'] += time
        unique_keys[key]['count'] += 1

    # Liste finali per le medie
    avg_dims, avg_times, avg_impls = [], [], []

    # Calcola la media per ogni chiave unica
    for (dim, impl), values in unique_keys.items():
        avg_dims.append(dim)
        avg_times.append(values['sum'] / values['count'])  # Media
        avg_impls.append(impl)

    # Trova il tempo minimo per ogni dimensione
    min_dims, min_times, min_impls = [], [], []
    seen_dims = set()  # Per tracciare le dimensioni già processate
    for dim, time, impl in zip(avg_dims, avg_times, avg_impls):
        if dim not in seen_dims:
            # Trova l'indice del minimo per la dimensione corrente
            indices = [i for i, d in enumerate(avg_dims) if d == dim]
            min_index = min(indices, key=lambda i: avg_times[i])  # Indice del tempo minimo
            # Aggiungi i valori minimi alle liste finali
            min_dims.append(avg_dims[min_index])
            min_times.append(avg_times[min_index])
            min_impls.append(avg_impls[min_index])
            seen_dims.add(dim)  # Marca la dimensione come processata

    # Scrivi i risultati nel file di output
    with open(output_file, mode='w', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(['Matrix Dimension', 'Min Time', 'Computation Option'])
        for dim, time, impl in zip(min_dims, min_times, min_impls):
            writer.writerow([dim, time, impl])

    print(f"Risultati salvati in {output_file}")
            
if __name__ == "__main__":
    main()

