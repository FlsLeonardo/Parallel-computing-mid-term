import matplotlib.pyplot as plt
# Elenco per memorizzare i dati delle due colonne
dimensioni = []
tempi = []

# Apri il file CSV
with open('../output/Omp.csv', mode='r', encoding='utf-8') as file:
    for riga in file:
        valori = riga.strip().split(";")
        dimensioni.append(int(valori[0]))  # La prima colonna (dimensioni)
        tempi.append(float(valori[1]))  # La seconda colonna (tempi)

tempi_per_dimensione = {}
# Raggruppa i tempi per dimensione
for dim, tempo in zip(dimensioni, tempi):
    if dim not in tempi_per_dimensione:
        tempi_per_dimensione[dim] = []
    tempi_per_dimensione[dim].append(tempo)

# Calcola la media dei tempi per ogni dimensione
dimensioni_uniche = []  #singole dimensioni
tempi_medi = []         #singoli tempi media per dimensione

for dim in tempi_per_dimensione:
    media_tempo = sum(tempi_per_dimensione[dim]) / len(tempi_per_dimensione[dim])
    dimensioni_uniche.append(dim)
    tempi_medi.append(media_tempo)
    
    
dati_ordinati = sorted(zip(dimensioni_uniche, tempi_medi)) #ordino i miei dati per dimensione
dimensioni_uniche, tempi_medi = zip(*dati_ordinati)

plt.plot(dimensioni_uniche, tempi_medi, marker='o', linestyle='-', color='r', label='Tempo medio')

# Aggiungi etichette agli assi
plt.xlabel('Dimensione della matrice (n)')
plt.ylabel('Tempo di trasposizione (secondi)')

# Aggiungi un titolo al grafico
plt.title('Tempo di Trasposizione in funzione della Dimensione della Matrice')

# Aggiungi una griglia (opzionale)
plt.grid(True)

# Aggiungi la legenda (opzionale)
plt.legend()

plt.savefig("../output/transpose_time_vs_matrix_size_Omp_32Threads.pdf", format='pdf')