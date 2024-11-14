#include "Functions.h"
#include <iostream>
#include <vector>
#include <omp.h>
using namespace std;

void myFunctionO() {
    cout << "OMP TRANSPOSE!" << endl;
}

void matTransposeOmp(vector<vector<float>>& M,int n,vector<vector<float>>& T){
#pragma omp parallel for collapse(2) num_threads(32)
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            T[j][i] = M[i][j];
        }
    }
}