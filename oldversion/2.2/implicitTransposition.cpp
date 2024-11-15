#include "Functions.h"
#include <iostream>
#include <vector>
using namespace std;

void myFunctionI() {
    std::cout << "IMPLICIT! Transposition" << std::endl;
}

void matTransposeImplicit(vector<vector<float>>& M,int n,vector<vector<float>>& T){
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            T[j][i] = M[i][j];
        }
    }
}