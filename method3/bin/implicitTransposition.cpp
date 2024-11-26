#include "Functions.h"
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

void myFunctionI() {
    std::cout << "IMPLICIT! Transposition" << std::endl;
}

void matTransposeImplicit(vector<vector<float>>& T,int n,int n_thread){
  for (int i = 0; i < n; ++i) {
        for (int j = i + 1; j < n; ++j) {
            float temp = T[i][j];
            T[i][j] = T[j][i];
            T[j][i] = temp;
        }
    } 
}
bool checkSymImplicit(const vector<vector<float>>& M,int n, int n_thread){
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