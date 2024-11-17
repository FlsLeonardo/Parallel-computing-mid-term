import sys
import matplotlib.pyplot as plt

def main():
    # Controllo se sono stati forniti parametri
    if len(sys.argv) < 2:
        print("Errore: Nessun parametro fornito.")
        print("Uso: python controllo_parametri.py <parametri>")
        sys.exit(1)
    for arg in sys.argv:
        if "--help" in arg:
            print("\nHai richiesto l'aiuto.")
            print("-type=(serial, implicit, omp)")
            print("-ES=(number)")
            sys.exit(0)
        if "-type" in arg:
            choice = sys.argv[1].split("=")[1]
            if choice not in ["serial", "implicit", "omp"]:
                print(f"Errore: Tipo '{choice}' non valido. Scegli tra 'serial', 'implicit' o 'omp'.")
                sys.exit(1)
            if choice == "serial":
                serial("../output/Serial.csv")
            elif choice == "implicit":
                implicit("../output/Implicit.csv")
            elif choice == "omp":
                omp("../output/Omp.csv")
        if "-ES" in arg: #efficency and Speedup
            matrix_dim = sys.argv[1].split("=")[1]
            efficency_speedup("../output/Omp.csv",matrix_dim)

def serial(filename):
    dimensioni = []
    tempi = []
    with open(filename, mode='r', encoding='utf-8') as file:
        for riga in file:
            valori = riga.strip().split(";")
            dimensioni.append(int(valori[0]))
            tempi.append(float(valori[1]))
        dati = sorted(zip(dimensioni, tempi))
        dimensioni, tempi = zip(*dati)
        plt.plot(dimensioni, tempi, marker='o', linestyle='-', color='r', label='Tempo medio')
        plt.xlabel('Dimensione della matrice (n)')
        plt.ylabel('Tempo di trasposizione (secondi)')
        plt.title('Tempo di Trasposizione Seriale in funzione della Dimensione della Matrice')
        plt.grid(True)
        plt.legend()
        #plt.show()
        plt.savefig("../output/transpose_time_vs_matrix_size_Serial.pdf", format='pdf')
    
def implicit(filename):
    dimensioni = []
    tempi = []
    compileropt = []
    with open(filename, mode='r', encoding='utf-8') as file:
        for riga in file:
            valori = riga.strip().split(";")
            dimensioni.append(int(valori[0]))
            tempi.append(float(valori[1]))
            compileropt.append(str(valori[2]))
            
    dati = sorted(zip(compileropt, dimensioni, tempi))
    compile_option, dimensioni, tempi = zip(*dati)
    print(compile_option)
    print(dimensioni)
    
    dim = [[],[],[]]                         #dimensione divisa in base ai compilatori 
    time = [[],[],[]]                        #tempo diviso in base ai compilatori 
    for opt, dim_, tempo in zip(compile_option, dimensioni, tempi):
        if opt == "O1":
            time[0].append(tempo)
            dim[0].append(dim_)
        elif opt == "O2":
            time[1].append(tempo)
            dim[1].append(dim_)
        elif opt == "O3":
            time[2].append(tempo)
            dim[2].append(dim_)
            
    plt.plot(dim[0], time[0], marker='o', linestyle='--', color='r', label='O1')
    plt.plot(dim[1], time[1], marker='o', linestyle='--', color='b', label='O2')
    plt.plot(dim[2], time[2], marker='o', linestyle='--', color='c', label='O3')
    plt.xlabel('Dimensione della matrice (n)')
    plt.ylabel('Tempo di trasposizione (secondi)')
    plt.title('Tempo di Trasposizione Implicito in funzione della Dimensione della Matrice')
    plt.grid(True)
    plt.legend()
    #plt.show()
    plt.savefig("../output/transpose_time_vs_matrix_size_Implicit.pdf", format='pdf')


def omp(filename):
    dimensioni = []
    tempi = []
    thread_n = []
    with open(filename, mode='r', encoding='utf-8') as file:
        for riga in file:
            valori = riga.strip().split(";")
            dimensioni.append(int(valori[0]))
            tempi.append(float(valori[1]))
            thread_n.append(str(valori[2]))
            
    dati = sorted(zip(thread_n, dimensioni, tempi))
    thread_n, dimensioni, tempi = zip(*dati)
    
    dim = [[],[],[],[],[],[],[],[]]                         #dimensione divisa in base ai num threads
    time = [[],[],[],[],[],[],[],[]]                          #tempo diviso in base ai num threads
    for nthread, dim_, tempo in zip(thread_n, dimensioni, tempi):
        if nthread == "1":
            time[0].append(tempo)
            dim[0].append(dim_)
        elif nthread == "2":
            time[1].append(tempo)
            dim[1].append(dim_)
        elif nthread == "4":
            time[2].append(tempo)
            dim[2].append(dim_)
        elif nthread == "8":
            time[3].append(tempo)
            dim[3].append(dim_)
        elif nthread == "16":
            time[4].append(tempo)
            dim[4].append(dim_)
        elif nthread == "32":
            time[5].append(tempo)
            dim[5].append(dim_)
        elif nthread == "64":
            time[6].append(tempo)
            dim[6].append(dim_)
        elif nthread == "96":
            time[7].append(tempo)
            dim[7].append(dim_)
            
    plt.plot(dim[0], time[0], marker='o', linestyle='--', color='#ff0000', label='1 thread')
    plt.plot(dim[1], time[1], marker='o', linestyle='--', color='#ff6100', label='2 thread')
    plt.plot(dim[2], time[2], marker='o', linestyle='--', color='#ffdc00', label='4 thread')
    plt.plot(dim[3], time[3], marker='o', linestyle='--', color='#55ff00', label='8 thread')
    plt.plot(dim[4], time[4], marker='o', linestyle='--', color='#00ecff', label='16 thread')
    plt.plot(dim[5], time[5], marker='o', linestyle='--', color='#0027ff', label='32 thread')
    plt.plot(dim[6], time[6], marker='o', linestyle='--', color='#ae00ff', label='64 thread')
    plt.plot(dim[7], time[7], marker='o', linestyle='--', color='#ff00f0', label='96 thread')
    plt.yscale("log")
    plt.xlabel('Dimensione della matrice (n)')
    plt.ylabel('Tempo di trasposizione (secondi)')
    plt.title('Tempo di Trasposizione Omp in funzione della Dimensione della Matrice')
    plt.grid(True)
    plt.legend()
    #plt.show()
    plt.savefig("../output/transpose_time_vs_matrix_size_Omp.pdf", format='pdf')
  
def efficency_speedup(filename,dim_matrix):
    matrix_times = []
    matrix_thread_used = []
    speedup = []
    efficency = []
    tempo_seriale = 0
    with open(filename, mode='r', encoding='utf-8') as file:
        for riga in file:
            dimension,time,n_thread = riga.strip().split(";")
            if dimension == dim_matrix:
                matrix_times.append(float(time))
                matrix_thread_used.append(int(n_thread))
    counter = 0;
    for i in matrix_thread_used:
        if i == 1:
            tempo_seriale = matrix_times[counter]
        counter = counter + 1
    
    dati = sorted(zip(matrix_thread_used, matrix_times))
    thread_n, tempi = zip(*dati)
        
    for nthread, tempo in zip(matrix_thread_used, matrix_times):
        speed = tempo_seriale / tempo
        speedup.append(speed)
        efficency.append(speed/nthread)
    print(matrix_thread_used)
    print(matrix_times)
    #print(speedup)
    #print(efficency)
    plt.figure(figsize=(10, 6))

    # Grafico per il tempo
    plt.subplot(3, 1, 1)  # 3 righe, 1 colonna, grafico 1
    plt.plot(matrix_thread_used, tempi, marker='o', color='b', label='Tempo (s)', linestyle='-', linewidth=2)
    plt.xlabel('Numero di Thread')
    plt.ylabel('Tempo (s)')
    plt.title('Tempo in funzione dei Thread')
    plt.grid(True)
    plt.legend()

    # Grafico per lo speedup
    plt.subplot(3, 1, 2)  # 3 righe, 1 colonna, grafico 2
    plt.plot(matrix_thread_used, speedup, marker='o', color='g', label='Speedup', linestyle='-', linewidth=2)
    plt.xlabel('Numero di Thread')
    plt.ylabel('Speedup')
    plt.title('Speedup in funzione dei Thread')
    plt.grid(True)
    plt.legend()

    # Grafico per l'efficienza
    plt.subplot(3, 1, 3)  # 3 righe, 1 colonna, grafico 3
    plt.plot(matrix_thread_used, efficency, marker='o', color='r', label='Efficienza', linestyle='-', linewidth=2)
    plt.xlabel('Numero di Thread')
    plt.ylabel('Efficienza')
    plt.title('Efficienza in funzione dei Thread')
    plt.grid(True)
    plt.legend()

    # Mostriamo il grafico
    plt.tight_layout()
    plt.show()
if __name__ == "__main__":
    main()
