#include "Functions.h"
#include <iostream>
#include <vector>
#include <omp.h>
#include <algorithm>
using namespace std;

void myFunctionO() {
    cout << "OMP TRANSPOSE!" << endl;
}

void matTransposeOmp(vector<vector<float>>& T,int n, int n_thread){
    #pragma omp parallel for num_threads(n_thread)
    for (int i = 0; i < n; ++i) {
        for (int j = i + 1; j < n; ++j) {
            float temp = T[i][j];
            T[i][j] = T[j][i];
            T[j][i] = temp;
        }
    } 
}

bool checkSymOmp(const vector<vector<float>>& M,int n, int n_thread){
    bool isSymmetric = true; // Shared flag to track symmetry

    #pragma omp parallel for collapse(2) num_threads(n_thread) 
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            if (M[i][j] != M[j][i]) {
                isSymmetric = false; // Update the shared flag
            }
        }
    }

    return isSymmetric;
}