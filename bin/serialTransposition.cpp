#include "Functions.h"
#include <iostream>
#include <vector>
using namespace std;

void myFunctionS() {
    std::cout << "SERIAL Transposition" << std::endl;
}

void matTransposeSerial(vector<vector<float>>& M,int n,vector<vector<float>>& T){
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            T[j][i] = M[i][j];
        }
    }
}