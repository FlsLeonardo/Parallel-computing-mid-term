#include "Functions.h"
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

void myFunctionS() {
    std::cout << "SERIAL Transposition" << std::endl;
}

void matTransposeSerial(vector<vector<float>>& T,int n,int n_thread){
    for (int i = 0; i < n; ++i) {
        for (int j = i + 1; j < n; ++j) {
            float temp = T[i][j];
            T[i][j] = T[j][i];
            T[j][i] = temp;
        }
    } 
}

bool checkSymSerial(const vector<vector<float>>& M,int n, int n_thread){
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