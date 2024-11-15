import pandas as pd
import matplotlib.pyplot as plt

# Leggi i dati dal file CSV senza intestazioni
file_path = "../output/Serial.csv"  # Sostituisci con il percorso corretto del file
df = pd.read_csv(file_path, header=None, delimiter=';')  # `header=None` specifica che il file non ha intestazioni

# Assegna nomi alle colonne
df.columns = ["Matrix_Size", "Transpose_Time"]

# Creazione del grafico
plt.figure(figsize=(10, 6))
plt.scatter(df["Matrix_Size"], df["Transpose_Time"], alpha=0.7, color='blue', label="Transpose Time")

# Impostazioni del grafico
plt.title("Matrix Transposition Time vs Matrix Size")
plt.xlabel("Matrix Size")
plt.ylabel("Transpose Time (seconds)")
plt.grid(True, linestyle="--", linewidth=0.5)
plt.legend()

# Salva il grafico come file PDF
output_pdf_path = "../output/transpose_time_vs_matrix_size_Serial.pdf"  # Percorso del file PDF di output
plt.savefig(output_pdf_path, format='pdf')

# Mostra il grafico (opzionale)
plt.show()