#include <iostream>
#include <vector>
#include <cstdlib>
#include <ctime>
#include <cmath>
#include <random>
#include <omp.h>
#include <fstream> // For file I/O
#include "Functions.h"
#define TEST 5

using namespace std;
void writeToFile(const string& filename,const int dim_matrix, const double text, string num_threads_or_type_of_compile_opt = "0");

void matTransposeSerial(vector<vector<float>>& M,int n,vector<vector<float>>& T, int n_thread,int n_block);      //implementations of functions in main program
void matTransposeImplicit(vector<vector<float>>& M,int n,vector<vector<float>>& T, int n_thread,int n_block);
void matTransposeOmp(vector<vector<float>>& M,int n,vector<vector<float>>& T, int n_thread,int n_block);

bool checkSymSerial(const vector<vector<float>>& M,int n, int n_thread);
bool checkSymImplicit(const vector<vector<float>>& M,int n, int n_thread);
bool checkSymOmp(const vector<vector<float>>& M,int n, int n_thread);

void (*matTranspose)(vector<vector<float>>& M,int n,vector<vector<float>>& T, int n_thread,int n_block) = nullptr;   // Puntatore alla funzione
bool (*checkSym)(const vector<vector<float>>& M,int n, int n_thread) = nullptr;


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

void writeToFile(const string& filename,const int dim_matrix, const double text, string num_threads_or_type_of_compile_opt) {
    ofstream file(filename,ios::app);
    if (!file.is_open()) {
        cerr << "Error: Could not open file " << filename << endl;
        return;
    }
    if(num_threads_or_type_of_compile_opt != "0"){
        file <<dim_matrix <<";"<< text <<";"<< num_threads_or_type_of_compile_opt <<"\n";
    }else{
        file <<dim_matrix <<";"<< text <<"\n";
    }
    file.close();
    if (file.fail()) {
        cerr << "Error: Failed to close file " << filename << endl;
        return;
    }
}

int main(int argc, char* argv[]) {
    if (argc != 3) {
        cerr << "Usage: " << argv[0] << " <matrix size>" << endl;
        return 1;
    }
    double wt1, wt2;  
    double Stime,Itime,Otime;                                           //for wall clock time
    int num = atoi(argv[1]);
    string compileOpt = argv[2];                                  // Dimensione della matrice passata come argomento
    int n = pow(2, num);
    int n_threads[8] = {1, 2, 4, 8, 16, 32, 64, 96};
    int n_blocks[1] = {256};
    vector<vector<float>> M(n, vector<float>(n));                // Creiamo una matrice n x n
    vector<vector<float>> T(n, vector<float>(n));                //Matrice Trasposta

    initializeMatrix(M, n);                                      // Inizializziamo la matrice con valori casuali
    //printMatrix(M,n);
    //printMatrix(T,n);
    cout <<"----------------------------------"<<endl; 
    cout << "Serial Implemenation"<< endl;
    checkSym = checkSymSerial;
    checkSym(M,n,1);
    for (int& block : n_blocks) {
        for (int i = 0; i < TEST; ++i) {
            //Serial implementation---------------------------------------------
            matTranspose = matTransposeSerial; 
            wt1 = omp_get_wtime();
            matTranspose(M,n,T,1,block);
            wt2 = omp_get_wtime();
            if(!checkTransposition(M,n,T)){cout<<"transpose not correct"<<endl;}
            Stime += (wt2 - wt1);
            writeToFile("../output/Serial.csv",num,(wt2 - wt1),to_string(block));//--------------------------------------------write file Serial
            writeToFile("../output/Implicit.csv",num,(wt2 - wt1),"Serial="+to_string(block));
        }
        cout <<" "<<num<< "\t" << (Stime/TEST)<< " sec\t" <<block<<endl;
        Stime= 0;
       } 
       cout <<endl;        
    cout << "Implicit Implemenation"<< endl; 
    checkSym = checkSymImplicit;
    checkSym(M,n,1);
    for (int& block : n_blocks) {
        for (int i = 0; i < TEST; ++i) {
             //Implicit implementation-------------------------------------------
            matTranspose = matTransposeImplicit; 
            wt1 = omp_get_wtime();
            matTranspose(M,n,T,1,block);
            wt2 = omp_get_wtime();
            if(!checkTransposition(M,n,T)){cout<<"transpose not correct"<<endl;}
            Itime += (wt2 - wt1);
            writeToFile("../output/Implicit.csv",num,(wt2 - wt1),compileOpt+"="+to_string(block)); //-----------------------------------------write file implicit
        }
        cout <<" "<<num<< "\t" << (Itime/TEST)<< " sec\t" <<block<<endl;  
        Itime= 0;
       } 
    cout <<endl;   
    cout << "Omp Implemenation"<< endl; 
    for (int& block : n_blocks) {  
      for (int& thread_count : n_threads) {
          checkSym = checkSymOmp;
          checkSym(M,n,thread_count);
          for (int i = 0; i < TEST; ++i) {
              //Omp implementation-------------------------------------------------
              matTranspose = matTransposeOmp; 

              wt1 = omp_get_wtime();
              matTranspose(M,n,T,thread_count,block);
              wt2 = omp_get_wtime();
              if(!checkTransposition(M,n,T)){cout<<"transpose not correct"<<endl;}
              Otime += (wt2 - wt1);
              writeToFile("../output/Omp.csv",num,(wt2 - wt1),"Thr="+to_string(thread_count)+" Blk="+to_string(block)); //---------------------------write file OMP
          }
          cout <<" "<<num<< "\t" << (Otime/TEST)<< " sec\t" <<thread_count<<" thread \t"<<block<<" blocksize"<<endl;
          Otime = 0;
      }    
    }
    return 0;
}