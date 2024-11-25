#include "Functions.h"
#include <iostream>
#include <vector>
using namespace std;

void myFunctionI() {
    std::cout << "IMPLICIT! Transposition" << std::endl;
}

void matTransposeImplicit(vector<vector<float>>& M,int n,vector<vector<float>>& T,int n_thread){
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
             T[j][i] = M[i][j];
        }
    }
}
bool checkSymImplicit(const vector<vector<float>>& M,int n){
    bool isSymmetric = true; 

    for (size_t i = 0; i < n; ++i) {
        for (size_t j = 0; j < n; ++j) {
            if (M[i][j] != M[j][i]) {
                isSymmetric = false;
            }
        }
    }

    return isSymmetric;
}