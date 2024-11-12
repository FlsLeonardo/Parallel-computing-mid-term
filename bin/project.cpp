#include <iostream>
#include <vector>
#include <cstdlib>
#include <ctime>
#include <cmath>
#include <random>

using namespace std;

// Funzione per inizializzare una matrice n x n con numeri casuali a virgola mobile
void initializeMatrix(vector<vector<float>>& matrix, int n) {
    // Inizializzazione del generatore di numeri casuali
    random_device rd;
    mt19937 gen(rd());  // Mersenne Twister engine
    uniform_real_distribution<> dis(0.0, 10.0);

    // Popolamento della matrice con valori casuali
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            float num = dis(gen);  // Numeri casuali tra 0 e 10
            matrix[i][j] = round(num* 100.0) / 100.0;
        }
    }
}

// Funzione per stampare la matrice con allineamento perfetto
void printMatrix(const vector<vector<float>>& matrix, int n) {
    const int width = 7;  // Larghezza per ogni numero (può essere cambiata)
    const int precision = 0;  // Numero di decimali (può essere cambiato)

    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            // Stampa ogni numero con una larghezza fissa, precisione e spazio uniforme
            std::cout << matrix[i][j]<<"\t";
        }
        std::cout << std::endl;  // A capo dopo ogni riga
    }
}

// Funzione per controllare se la matrice è simmetrica
bool checkSymmetry(const vector<vector<float>>& matrix, int n) {
    for (int i = 0; i < n; ++i) {
        for (int j = i + 1; j < n; ++j) {  // Controlliamo solo la parte superiore della matrice (i < j)
            if (matrix[i][j] != matrix[j][i]) {
                return false;  // Se c'è una disuguaglianza, la matrice non è simmetrica
            }
        }
    }
    return true;  // Se tutte le verifiche passano, la matrice è simmetrica
}

int main(int argc, char* argv[]) {
    if (argc != 2) {
        std::cerr << "Usage: " << argv[0] << " <matrix size>" << std::endl;
        return 1;
    }

    int n = std::atoi(argv[1]);  // Dimensione della matrice passata come argomento

    // Creiamo una matrice n x n
    std::vector<std::vector<float>> matrix(n, std::vector<float>(n));

    // Inizializziamo la matrice con valori casuali
    initializeMatrix(matrix, n);

    // Stampiamo la matrice
    std::cout << "Randomly initialized matrix:" << std::endl;
    printMatrix(matrix, n);

    // Controlliamo se la matrice è simmetrica
    if (checkSymmetry(matrix, n)) {
        std::cout << "The matrix is symmetric." << std::endl;
    } else {
        std::cout << "The matrix is not symmetric." << std::endl;
    }

    return 0;
}
