import sys
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from collections import defaultdict

def main():
    # Controllo se sono stati forniti parametri
    if len(sys.argv) < 2:
        print("Nessun parametro fornito.")
        serial("../output/Serial.csv")
        omp("../output/Omp.csv")
        speedup("../output/Omp.csv")
        efficiency("../output/Omp.csv")
        implicit("../output/Implicit.csv")
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
    # Leggi i dati dal file
    matrix_size = []
    transpose_time = []
    blocks = []
    
    # Apri il file e leggi le righe
    with open(filename, 'r') as file:
        for line in file:
            # Dividi ogni linea usando il punto e virgola
            data = line.strip().split(';')
            # Aggiungi i dati alle rispettive liste
            matrix_size.append(int(data[0]))
            transpose_time.append(float(data[1]))
            blocks.append(int(data[2]))
    result = media(matrix_size, transpose_time, blocks)
    matrix_size, transpose_time, blocks = zip(*result)
    # Converti le liste in array numpy
    matrix_size = np.array(matrix_size)
    transpose_time = np.array(transpose_time)
    blocks = np.array(blocks)

    # Plot il grafico separando le linee per ciascun blocco
    plt.figure(figsize=(10, 6))

    # Blocchi unici
    unique_blocks = np.unique(blocks)

    # Traccia una linea per ogni blocco
    for block in unique_blocks:
        # Filtra i dati per il blocco corrente
        block_data = [(m, t) for m, t, b in zip(matrix_size, transpose_time, blocks) if b == block]
        block_matrix_size, block_transpose_time = zip(*block_data)
        
        # Traccia la linea
        plt.plot(block_matrix_size, block_transpose_time, label=f'Block Size {block}', marker='o')

    # Aggiungi etichette e titolo
    #plt.yscale("log")
    plt.xlabel('Matrix Size')
    plt.ylabel('Transpose Time (seconds)')
    plt.title('Matrix Transpose Time vs Matrix Size for Different Block Sizes')

    # Aggiungi la legenda
    plt.legend(title="Block Size")

    # Aggiungi la griglia
    plt.grid(True)

    # Mostra il grafico
    #plt.show()
    plt.savefig("../pdf_graph/transpose_time_vs_matrix_size_Serial.pdf", format='pdf')
    plt.clf()
    
def implicit(filename, filter_keyword=None, colors=None):
    # Lista colori predefinita se non specificata
    if colors is None:
        colors = ['#ff0000', '#ff6100', '#ffdc00', '#55ff00', '#00ecff', 
                  '#0027ff', '#ae00ff', '#ff00f0', '#C70039', '#FFB6C1']

    # Leggi il file CSV
    data = pd.read_csv(filename, sep=';', header=None, names=['X', 'Y', 'Type'])

    # Estrai la parte prima dell'uguale e la parte dopo
    data[['Group', 'Value']] = data['Type'].str.extract(r'([A-Za-z0-9]+(?:\s*-?[A-Za-z0-9-]+)*)=(\d+)')

    # Filtra i dati se un filtro è specificato
    if filter_keyword:
        data = data[data['Group'].str.contains(filter_keyword)]

    # Trova tutti i gruppi distinti (es. O2, O3, etc.)
    unique_groups = data['Group'].unique()

    # Crea il grafico
    plt.figure(figsize=(12, 8))

    # Colore ciclico
    color_index = 0

    # Itera attraverso ciascun gruppo (O2, O3, etc.)
    for group in unique_groups:
        # Filtra i dati per il gruppo corrente (es. O2)
        group_data = data[data['Group'] == group]

        # Raggruppa per 'Value' (es. 120, 155) e 'X' (dimensione della matrice)
        grouped_data = group_data.groupby(['Value', 'X'])['Y'].mean().reset_index()

        # Traccia ogni configurazione (es. O2=120, O2=155, etc.)
        for value, group_subset in grouped_data.groupby('Value'):
            # Colore ciclico per ogni linea
            color = colors[color_index % len(colors)]
            plt.plot(group_subset['X'], group_subset['Y'], marker='o', linestyle='--',label=f"{group}={value}", color=color)
            color_index += 1  # Incrementa l'indice del colore

    # Personalizza il grafico
    plt.yscale("log")  # Usa una scala logaritmica per visualizzare meglio i dati
    plt.title("Tempi medi per dimensione della matrice, per ciascun gruppo (O2, O3, etc.)", fontsize=16)
    plt.xlabel("Dimensione della matrice (X)", fontsize=14)
    plt.ylabel("Tempi medi di esecuzione (Y)", fontsize=14)
    plt.legend(title="Configurazioni", loc='upper left', bbox_to_anchor=(1, 1))
    plt.grid(True)

    # Salva il grafico come PDF
    plt.tight_layout()
    plt.savefig(f"../pdf_graph/transpose_time_vs_matrix_size_Implicit.pdf", format='pdf')
    plt.clf()  # Pulisce la figura dopo averla salvata

def omp(filename, colors=None):
    dimensioni = []
    tempi = []
    thread_n = []
    
    # Colori predefiniti se non forniti
    if colors is None:
        colors = ['#ff0000', '#ff6100', '#ffdc00', '#55ff00', '#00ecff', 
                  '#0027ff', '#ae00ff', '#ff00f0', '#C70039', '#FFB6C1']
    
    # Leggi i dati dal file
    with open(filename, mode='r', encoding='utf-8') as file:
        for riga in file:
            valori = riga.strip().split(";")
            dimensioni.append(int(valori[0]))  # Dimensione della matrice
            tempi.append(float(valori[1]))     # Tempo di esecuzione
            # Separazione della parte "Thr=96" e "Blk=2048"
            thread_info = valori[2]
            threads, blocksize = thread_info.split()  # separa "Thr=96" e "Blk=2048"
            num_threads = threads.split('=')[1]  # estrae "96" da "Thr=96"
            block_size = blocksize.split('=')[1]  # estrae "2048" da "Blk=2048"
            thread_n.append(f"Thr={num_threads} Blk={block_size}")  # Memorizza i thread e blocco

    # Calcola la media dei tempi per dimensioni e tipi
    result = media(dimensioni, tempi, thread_n)
    dimensioni, tempi, thread_n = zip(*result)  # Decomponi i risultati in tre liste separate

    # Raggruppa i dati per tipo (numero di thread e dimensione del blocco)
    grouped_data = defaultdict(list)
    for dim, tempo, tipo in zip(dimensioni, tempi, thread_n):
        grouped_data[tipo].append((dim, tempo))

    # Crea il grafico
    plt.figure(figsize=(12, 8))

    # Lista di colori
    color_index = 0  # Indice per tracciare i colori

    # Traccia ogni gruppo (per ogni combinazione di numero di thread e dimensione del blocco)
    for tipo, values in grouped_data.items():
        values.sort()  # Ordina per dimensione (per avere una linea più ordinata)
        dimensioni_sorted, tempi_sorted = zip(*values)  # Separazione dimensioni e tempi

        # Usa il colore dal lista, ciclando quando i colori sono terminati
        color = colors[color_index % len(colors)]  # Seleziona colore ciclicamente
        plt.plot(dimensioni_sorted, tempi_sorted, marker='o',linestyle='--', label=f"{tipo}", color=color)  # Usa 'Thr' e 'Blk' come label
        color_index += 1  # Incrementa l'indice del colore

    # Aggiungi etichette e titolo
    plt.xlabel('Dimensioni della Matrice', fontsize=14)
    plt.ylabel('Tempi di esecuzione (in secondi)', fontsize=14)
    plt.title('Tempi per Dimensione della Matrice, Numero di Thread e Blocksize', fontsize=16)
    plt.legend(title="Configurazione", loc='upper left', bbox_to_anchor=(1, 1))
    plt.yscale("log")
    # Mostra la griglia e salva il grafico come PDF
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("../pdf_graph/transpose_time_vs_matrix_size_Omp.pdf", format='pdf', dpi=300)
    plt.clf()  # Pulisce la figura dopo averla salvata


def speedup(filename):
    # Crea le liste per raccogliere i dati
    dim = []  # Lista per le dimensioni delle matrici
    time = []  # Lista per i tempi di esecuzione
    thr_blk = []  # Lista per le configurazioni "Thr=XX Blk=XX"

    # Leggi i dati dal file
    with open(filename, mode='r', encoding='utf-8') as file:
        for line in file:
            values = line.strip().split(';')

            # Controllo sul numero di colonne
            if len(values) < 3:
                continue  # Se la riga non ha almeno 3 colonne, salta

            # Estrai i valori e aggiungili alle liste
            dimm = int(values[0])  # Prima colonna: dimensione matrice
            timee = float(values[1])  # Seconda colonna: tempo di esecuzione
            thr_blk_value = values[2]  # Terza colonna: configurazione (e.g., Thr=96 Blk=512)

            # Aggiungi i valori alle rispettive liste
            dim.append(dimm)
            time.append(timee)
            thr_blk.append(thr_blk_value)

    # Calcola la media dei tempi per ogni combinazione di (dim, blk)
    result = media(dim, time, thr_blk)
    
    # Estrai le tre liste finali (dim, time e thr_blk)
    dim, time, thr_blk = zip(*result)  # Unpack the results into three separate lists

    # Ora calcoliamo lo speedup
    serial_times = {}  # Per memorizzare il tempo seriale per ogni dimensione
    for d, t, _ in zip(dim, time, thr_blk):
        if d not in serial_times:
            serial_times[d] = t  # Il primo tempo per ogni dim è considerato come seriale

    # Calcolare lo speedup
    speedup = [serial_times[d] / t for d, t in zip(dim, time)]

    # Creiamo il grafico con una figura più grande
    plt.figure(figsize=(20, 12))  # Aumenta ulteriormente la dimensione della figura per fare più spazio

    # Dizionario per raggruppare i dati per (dim, blk)
    grouped_data = defaultdict(list)

    # Raggruppiamo i dati per (dim, blk) e memorizziamo i (thread, speedup)
    for (d, blk), t, s in zip(zip(dim, thr_blk), time, speedup):
        # Estrai il numero di thread dalla configurazione 'Thr=XX'
        threads = int(blk.split('Thr=')[1].split()[0])  # Estrai numero di thread
        # Estrarre la blocksize (Blk=XX) dalla configurazione
        blocksize = int(blk.split('Blk=')[1])  # Estrai la blocksize
        grouped_data[(d, blocksize)].append((threads, s))  # Raggruppa per dim e blocksize

    # Lista di colori per le linee
    colors = ['#ff0000', '#ff6100', '#ffdc00', '#55ff00', '#00ecff', '#0027ff', '#ae00ff', '#ff00f0', '#C70039', '#FFB6C1']
    color_index = 0  # Indice per tracciare i colori

    # Traccia i dati per ogni combinazione di (dim, blk)
    for (d, blk), values in grouped_data.items():
        # Ordina i valori per numero di thread
        values.sort(key=lambda x: x[0])
        threads, speedups = zip(*values)  # Separare thread e speedup
        # Usa il colore dal lista, ciclando quando i colori sono terminati
        color = colors[color_index % len(colors)]  # Seleziona colore ciclicamente
        plt.plot(threads, speedups, marker='o',linestyle='--', label=f'Dim={d} Blk={blk}', color=color)  # Applica il colore
        color_index += 1  # Incrementa l'indice del colore

    # Impostiamo le etichette
    plt.xlabel("Numero di Thread", fontsize=14)
    plt.ylabel("Speedup", fontsize=14)
    plt.title("Speedup vs Numero di Thread per Configurazioni di Matrice e Blocksize", fontsize=16)

    # Aggiungiamo la legenda e la griglia
    plt.legend(title="Configurazioni (Dim, Blk)", loc='upper left', bbox_to_anchor=(1, 1))  # Posizione della legenda a sinistra
    plt.grid(True)

    # Regola la disposizione del grafico per aggiungere spazio alla legenda
    plt.subplots_adjust(right=0.85)  # Aggiungi spazio sulla destra per la legenda

    plt.savefig("../pdf_graph/speedup_plot.pdf", format='pdf')  # Usa bbox_inches='tight' per evitare il taglio
    #plt.show()

    
def efficiency(filename, colors=None):
    # Crea le liste per raccogliere i dati
    dim = []  # Lista per le dimensioni delle matrici
    time = []  # Lista per i tempi di esecuzione
    thr_blk = []  # Lista per le configurazioni "Thr=XX Blk=XX"

    # Colori predefiniti se non forniti
    if colors is None:
        colors = ['#ff0000', '#ff6100', '#ffdc00', '#55ff00', '#00ecff', 
                  '#0027ff', '#ae00ff', '#ff00f0', '#C70039', '#FFB6C1']

    # Leggi i dati dal file
    with open(filename, mode='r', encoding='utf-8') as file:
        for line in file:
            values = line.strip().split(';')

            # Controllo sul numero di colonne
            if len(values) < 3:
                continue  # Se la riga non ha almeno 3 colonne, salta

            # Estrai i valori e aggiungili alle liste
            dimm = int(values[0])  # Prima colonna: dimensione matrice
            timee = float(values[1])  # Seconda colonna: tempo di esecuzione
            thr_blk_value = values[2]  # Terza colonna: configurazione (e.g., Thr=96 Blk=512)

            # Aggiungi i valori alle rispettive liste
            dim.append(dimm)
            time.append(timee)
            thr_blk.append(thr_blk_value)

    # Calcola la media dei tempi per ogni combinazione di (dim, blk)
    result = media(dim, time, thr_blk)
    
    # Estrai le tre liste finali (dim, time e thr_blk)
    dim, time, thr_blk = zip(*result)  # Unpack the results into three separate lists

    # Ora calcoliamo lo speedup
    serial_times = {}  # Per memorizzare il tempo seriale per ogni dimensione
    for d, t, _ in zip(dim, time, thr_blk):
        if d not in serial_times:
            serial_times[d] = t  # Il primo tempo per ogni dim è considerato come seriale

    # Calcolare lo speedup
    speedup = [serial_times[d] / t for d, t in zip(dim, time)]

    # Calcolare l'efficienza
    efficiency = []
    for s, blk in zip(speedup, thr_blk):
        # Estrai il numero di thread dalla configurazione 'Thr=XX'
        threads = int(blk.split('Thr=')[1].split()[0])  # Estrai numero di thread
        if threads == 0:
            eff = 0  # Se per qualche motivo c'è un errore nel numero di thread, mettiamo efficienza a 0
        else:
            eff = s / threads * 100  # Efficienza = speedup / numero di thread
        efficiency.append(eff)

    # Creiamo il grafico con una figura più grande
    plt.figure(figsize=(20, 12))  # Aumenta ulteriormente la dimensione della figura per fare più spazio

    # Dizionario per raggruppare i dati per (dim, blk)
    grouped_data = defaultdict(list)

    # Raggruppiamo i dati per (dim, blk) e memorizziamo i (thread, efficiency)
    for (d, blk), t, e in zip(zip(dim, thr_blk), time, efficiency):
        # Estrai il numero di thread dalla configurazione 'Thr=XX'
        threads = int(blk.split('Thr=')[1].split()[0])  # Estrai numero di thread
        # Estrarre la blocksize (Blk=XX) dalla configurazione
        blocksize = int(blk.split('Blk=')[1])  # Estrai la blocksize
        grouped_data[(d, blocksize)].append((threads, e))  # Raggruppa per dim e blocksize

    # Lista di colori
    color_index = 0  # Indice per tracciare i colori

    # Traccia i dati per ogni combinazione di (dim, blk)
    for (d, blk), values in grouped_data.items():
        # Ordina i valori per numero di thread
        values.sort(key=lambda x: x[0])
        threads, efficiencies = zip(*values)  # Separare threads e efficiency
        # Usa il colore dal lista, ciclando quando i colori sono terminati
        color = colors[color_index % len(colors)]  # Seleziona colore ciclicamente
        plt.plot(threads, efficiencies, marker='o',linestyle='--', label=f'Dim={d} Blk={blk}', color=color)  # Applica il colore
        color_index += 1  # Incrementa l'indice del colore

    # Impostiamo le etichette
    plt.xlabel("Numero di Thread", fontsize=14)
    plt.ylabel("Efficienza (%)", fontsize=14)
    plt.title("Efficienza vs Numero di Thread per Configurazioni di Matrice e Blocksize", fontsize=16)

    # Aggiungiamo la legenda e la griglia
    plt.legend(title="Configurazioni (Dim, Blk)", loc='upper left', bbox_to_anchor=(1, 1))  # Posizione della legenda a sinistra
    plt.grid(True)

    # Regola la disposizione del grafico per aggiungere spazio alla legenda
    plt.subplots_adjust(right=0.85)  # Aggiungi spazio sulla destra per la legenda

    plt.savefig("../pdf_graph/efficiency_plot.pdf", format='pdf')  # Usa bbox_inches='tight' per evitare il taglio
    #plt.show()
    
def media(dimensione, tempi, tipo):
    dati_raggruppati = defaultdict(list)

    # Raggruppiamo i tempi in base ai valori della dimensione e tipo
    for dim, t, tpo in zip(dimensione, tempi, tipo):
        dati_raggruppati[(dim, tpo)].append(t)

    # Ora calcoliamo la media per ciascun gruppo e salviamo i risultati
    risultati = []

    for (dim, tpo), tempi_gruppo in dati_raggruppati.items():
        media_tempi = np.mean(tempi_gruppo)  # Calcoliamo la media dei tempi per il gruppo
        risultati.append((dim, media_tempi, tpo))

    # Risultati finali
    for r in risultati:
        print(f"Dimensione: {r[0]}, Media tempi: {r[1]}, Tipo: {r[2]}")
    return risultati
    
if __name__ == "__main__":
    main()
