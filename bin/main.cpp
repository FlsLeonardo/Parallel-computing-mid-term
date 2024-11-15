#include <iostream>
#include <vector>
#include <cstdlib>
#include <ctime>
#include <cmath>
#include <random>
#include <omp.h>
#include "Functions.h"

using namespace std;

void matTransposeSerial(vector<vector<float>>& M,int n,vector<vector<float>>& T);      //implementations of functions in main program
void matTransposeImplicit(vector<vector<float>>& M,int n,vector<vector<float>>& T);
void matTransposeOmp(vector<vector<float>>& M,int n,vector<vector<float>>& T);

bool checkSymSerial(const vector<vector<float>>& M,int n);
bool checkSymImplicit(const vector<vector<float>>& M,int n);
bool checkSymOmp(const vector<vector<float>>& M,int n);

void (*matTranspose)(vector<vector<float>>& M,int n,vector<vector<float>>& T) = nullptr;   // Puntatore alla funzione
bool (*checkSym)(const vector<vector<float>>& M,int n) = nullptr;


void initializeMatrix(vector<vector<float>>& matrix, int n) {     // Funzione per inizializzare una matrice n x n con numeri casuali a virgola mobile
    random_device rd;                                             // Inizializzazione del generatore di numeri casuali
    mt19937 gen(rd());
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

bool checkTransposition(const vector<vector<float>>& M,int n,const vector<vector<float>>& T) {
    for (size_t i = 0; i < n; ++i) {
        for (size_t j = 0; j < n; ++j) {
            if (M[j][i] != T[i][j]) {
                return false;
            }
        }
    }

    return true;
}

int main(int argc, char* argv[]) {
    if (argc != 2) {
        std::cerr << "Usage: " << argv[0] << " <matrix size>" << std::endl;
        return 1;
    }
    double wt1, wt2;                                             //for wall clock time
    int n = std::atoi(argv[1]);                                  // Dimensione della matrice passata come argomento
    n = pow(2, n);
    vector<vector<float>> M(n, vector<float>(n));                // Creiamo una matrice n x n
    vector<vector<float>> T(n, vector<float>(n));                //Matrice Trasposta

    initializeMatrix(M, n);                                      // Inizializziamo la matrice con valori casuali
    //printMatrix(M,n);

    //Serial implementation
    matTranspose = matTransposeSerial;
    checkSym = checkSymSerial;
    cout << "Serial ceck symmetry" <<checkSym(M,n)<< endl;
    wt1 = omp_get_wtime();
    //checkSym(M,n);
    matTranspose(M,n,T);
    wt2 = omp_get_wtime();
    cout << "Check Transposition " <<checkTransposition(M,n,T)<< endl;
    cout << "Serial wall clock time (omp_get_wtime) = " << (wt2 - wt1) << " sec" << endl<<endl;


    //printMatrix(T,n);

    //Implicit implementation
    matTranspose = matTransposeImplicit;
    checkSym = checkSymImplicit;
    cout << "Implicit ceck symmetry" <<checkSym(M,n)<< endl;
    wt1 = omp_get_wtime();
    //checkSym(M,n);
    matTranspose(M,n,T);
    wt2 = omp_get_wtime();
    cout << "Check Transposition " <<checkTransposition(M,n,T)<< endl;
    cout << "Implicit wall clock time (omp_get_wtime) = " << (wt2 - wt1) << " sec" << endl<<endl;
    //printMatrix(T,n);

    //Omp implementation
    matTranspose = matTransposeOmp;
    checkSym = checkSymOmp;
    cout << "Omp ceck symmetry" <<checkSym(M,n)<< endl;
    wt1 = omp_get_wtime();
    //checkSym(M,n);
    matTranspose(M,n,T);
    wt2 = omp_get_wtime();
    cout << "Check Transposition " <<checkTransposition(M,n,T)<< endl;
    cout << "Omp wall clock time (omp_get_wtime) = " << (wt2 - wt1) << " sec" << endl<<endl;
    //printMatrix(T,n);


    return 0;
}