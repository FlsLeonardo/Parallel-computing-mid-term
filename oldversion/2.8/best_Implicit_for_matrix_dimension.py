import sys
import pandas as pd
import numpy as np
import csv


def main():
    # Controllo se sono stati forniti parametri
    if len(sys.argv) < 2:
        compare("./method1/output/Implicit.csv","./method2/output/Implicit.csv","./method3/output/Implicit.csv","best.csv")
        sys.exit(1)
    for arg in sys.argv:
        if "--help" in arg:
            print("\nHai richiesto l'aiuto.")
            print("-type=(serial, implicit, omp)")
            print("-ES=(number)")
            sys.exit(0)
    

def compare(file1, file2, file3, output_file):
    # Leggi i file CSV separati da punto e virgola
    df1 = pd.read_csv(file1, sep=';', header=None, names=["Dimensione", "Tempo", "Implementazione"])
    df2 = pd.read_csv(file2, sep=';', header=None, names=["Dimensione", "Tempo", "Implementazione"])
    df3 = pd.read_csv(file3, sep=';', header=None, names=["Dimensione", "Tempo", "Implementazione"])

    # Unisci i tre DataFrame riga per riga (concatenazione)
    df_combined = pd.concat([df1, df2, df3], ignore_index=True)
    
    # Converti il DataFrame in un array bidimensionale
    result_array = df_combined.values
    print(result_array)
    time_dict = {}

    for row in result_array:
        matrix_dim = row[0]  
        time = row[1]        
        comp_opt = row[2]   
        if matrix_dim not in time_dict:
            time_dict[matrix_dim] = []
        time_dict[matrix_dim].append((time, comp_opt))
    with open('best.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Matrix Dimension', 'Min Time', 'Computation Option'])
        for matrix_dim, times_options in time_dict.items():
            min_time, comp_opt = min(times_options, key=lambda x: x[0])
            writer.writerow([matrix_dim, min_time, comp_opt])
            
if __name__ == "__main__":
    main()

