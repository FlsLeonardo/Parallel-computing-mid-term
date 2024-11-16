#include <iostream>
#include <vector>
#include <cstdlib>
#include <ctime>
#include <cmath>
#include <random>
#include <omp.h>
#include <fstream> // For file I/O
#include "Functions.h"
#define TEST 15

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
void printMatrix(const vector<vector<float>>& matrix, int n) {                                        // Numero di decimali (può essere cambiato)
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {                                 // Stampa ogni numero con una larghezza fissa, precisione e spazio uniforme                           
            cout << matrix[i][j]<<"\t";
        }
        cout << endl;  
    }
}

bool checkTransposition(const vector<vector<float>>& M,int n,const vector<vector<float>>& T) {
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            if (M[j][i] != T[i][j]) {
                return false;
            }
        }
    }
    return true;
}

void writeToFile(const string& filename,const int dim_matrix, const double text) {
    ofstream file(filename,ios::app);
    if (!file.is_open()) {
        cerr << "Error: Could not open file " << filename << endl;
        return;
    }
    file <<dim_matrix <<";"<< text <<"\n";
    file.close();
    if (file.fail()) {
        cerr << "Error: Failed to close file " << filename << endl;
        return;
    }
}

int main(int argc, char* argv[]) {
    if (argc != 2) {
        cerr << "Usage: " << argv[0] << " <matrix size>" << endl;
        return 1;
    }
    double wt1, wt2;  
    double Stime,Itime,Otime;                                           //for wall clock time
    int n = atoi(argv[1]);                                  // Dimensione della matrice passata come argomento
    n = pow(2, n);
    vector<vector<float>> M(n, vector<float>(n));                // Creiamo una matrice n x n
    vector<vector<float>> T(n, vector<float>(n));                //Matrice Trasposta

    initializeMatrix(M, n);                                      // Inizializziamo la matrice con valori casuali
    //printMatrix(M,n);
    //printMatrix(T,n);                                 

    for (int i = 0; i < TEST; ++i) {
        //Serial implementation
        matTranspose = matTransposeSerial; 
        //checkSym = checkSymSerial;
        //checkSym(M,n);
        wt1 = omp_get_wtime();
        matTranspose(M,n,T);
        wt2 = omp_get_wtime();
        //checkTransposition(M,n,T);
        Stime += (wt2 - wt1);
        writeToFile("../output/Serial.csv",n,(wt2 - wt1));
        
        //Implicit implementation
        matTranspose = matTransposeImplicit; 
        //checkSym = checkSymImplicit;
        //checkSym(M,n);
        wt1 = omp_get_wtime();
        matTranspose(M,n,T);
        wt2 = omp_get_wtime();
        //checkTransposition(M,n,T);
        Itime += (wt2 - wt1);
        writeToFile("../output/Implicit.csv",n,(wt2 - wt1));
        
        //Omp implementation
        matTranspose = matTransposeOmp; 
        //checkSym = checkSymOmp;
        //checkSym(M,n);
        wt1 = omp_get_wtime();
        matTranspose(M,n,T);
        wt2 = omp_get_wtime();
        //checkTransposition(M,n,T);
        Otime += (wt2 - wt1);
        writeToFile("../output/Omp.csv",n,(wt2 - wt1));
    }
    cout << "Serial wall clock time (omp_get_wtime) = " << (Stime/TEST)<< " sec" << endl<<endl;
    cout << "Implicit wall clock time (omp_get_wtime) = " << (Itime/TEST)<< " sec" << endl<<endl;
    cout << "Omp wall clock time (omp_get_wtime) = " << (Otime/TEST)<< " sec" << endl<<endl;
    return 0;
}