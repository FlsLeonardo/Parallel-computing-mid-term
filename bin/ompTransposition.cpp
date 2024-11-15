#include "Functions.h"
#include <iostream>
#include <vector>
#include <omp.h>
using namespace std;

void myFunctionO() {
    cout << "OMP TRANSPOSE!" << endl;
}

void matTransposeOmp(vector<vector<float>>& M,int n,vector<vector<float>>& T){
#pragma omp parallel for collapse(2) num_threads(16)
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            T[j][i] = M[i][j];
        }
    }
}

bool checkSymOmp(const vector<vector<float>>& M,int n){
    bool isSymmetric = true; // Shared flag to track symmetry
    #pragma omp parallel for collapse(2) num_threads(1)
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < n; ++j) {
                if (M[i][j] != M[j][i]) {
                    isSymmetric = false; // Update the shared flag
                }
            }
        }
    return isSymmetric;
}