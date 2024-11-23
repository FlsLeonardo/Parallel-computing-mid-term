#include <iostream>
#include <vector>
#include <cstdlib>
#include <ctime>
#include <cmath>
#include <random>
#include <omp.h>
#include "Functions.h"

using namespace std;

vector<vector<float>> matTransposeSerial(const vector<vector<float>>& M);      //implementations of functions in main program
vector<vector<float>> matTransposeImplicit(const vector<vector<float>>& M);
vector<vector<float>> matTransposeOmp(const vector<vector<float>>& M);

vector<vector<float>> (*matTranspose)(const vector<vector<float>>& M) = nullptr;   // Puntatore alla funzione


void initializeMatrix(vector<vector<float>>& matrix, int n) {     // Funzione per inizializzare una matrice n x n con numeri casuali a virgola mobile

    // Inizializzazione del generatore di numeri casuali
    random_device rd;
    mt19937 gen(rd());                                            // Mersenne Twister engine
    uniform_real_distribution<> dis(0.0, 10.0);


    for (int i = 0; i < n; ++i) {                                  // Popolamento della matrice con valori casuali
        for (int j = 0; j < n; ++j) {
            float num = dis(gen);                                  // Numeri casuali tra 0 e 10
            matrix[i][j] = round(num* 100.0) / 100.0;
        }
    }
}

// Funzione per stampare la matrice con allineamento perfetto
void printMatrix(const vector<vector<float>>& matrix, int n) {
    const int width = 7;                                              // Larghezza per ogni numero (può essere cambiata)
    const int precision = 0;                                          // Numero di decimali (può essere cambiato)

    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {                                 // Stampa ogni numero con una larghezza fissa, precisione e spazio uniforme
            std::cout << matrix[i][j]<<"\t";
        }
        std::cout << std::endl;
    }
}

// Funzione per controllare se la matrice è simmetrica
bool checkSymmetry(const vector<vector<float>>& matrix, int n) {
    for (int i = 0; i < n; ++i) {
        for (int j = i + 1; j < n; ++j) {                           // Controlliamo solo la parte superiore della matrice (i < j)
            if (matrix[i][j] != matrix[j][i]) {
                return false;                                       // Se c'è una disuguaglianza, la matrice non è simmetrica
            }
        }
    }
    return true;                                                    // Se tutte le verifiche passano, la matrice è simmetrica
}


int main(int argc, char* argv[]) {
    if (argc != 2) {
        std::cerr << "Usage: " << argv[0] << " <matrix size>" << std::endl;
        return 1;
    }
    double wt1, wt2;                                             //for wall clock time
    int n = std::atoi(argv[1]);                                  // Dimensione della matrice passata come argomento

    vector<vector<float>> M(n, vector<float>(n));                // Creiamo una matrice n x n

    initializeMatrix(M, n);                                      // Inizializziamo la matrice con valori casuali

    matTranspose = matTransposeSerial; //Serial implementation
    wt1 = omp_get_wtime();
    vector<vector<float>> T = matTranspose(M);
    wt2 = omp_get_wtime();
    cout << "Serial wall clock time (omp_get_wtime) = " << (wt2 - wt1) << " sec" << std::endl;

    matTranspose = matTransposeImplicit; //Implicit implementation
    wt1 = omp_get_wtime();
    T = matTranspose(M);
    wt2 = omp_get_wtime();
    cout << "Implicit wall clock time (omp_get_wtime) = " << (wt2 - wt1) << " sec" << std::endl;

    matTranspose = matTransposeOmp; //Omp implementation
    wt1 = omp_get_wtime();
    T = matTranspose(M);
    wt2 = omp_get_wtime();
    cout << "Omp wall clock time (omp_get_wtime) = " << (wt2 - wt1) << " sec" << std::endl;


    return 0;
}