#include "Functions.h"
#include <iostream>
#include <vector>
#include <omp.h>
using namespace std;

void myFunctionO() {
    cout << "OMP TRANSPOSE!" << endl;
}

void matTransposeOmp(vector<vector<float>>& M,int n,vector<vector<float>>& T, int n_thread,int n_block){
    #pragma omp parallel for collapse(2) num_threads(n_thread)
    for (int i_block = 0; i_block < n; i_block += n_block) {
        for (int j_block = 0; j_block < n; j_block += n_block) {
            for (int i = i_block; i < min(i_block + n_block, n); ++i) {
                for (int j = j_block; j < min(j_block + n_block, n); ++j) {
                    T[j][i] = M[i][j];
                }
            }
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