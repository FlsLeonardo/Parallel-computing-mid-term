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
                
            
if __name__ == "__main__":
    main()
