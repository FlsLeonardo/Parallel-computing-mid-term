#include "Functions.h"
#include <iostream>
#include <vector>
using namespace std;

void myFunctionS() {
    std::cout << "SERIAL Transposition" << std::endl;
}

void matTransposeSerial(vector<vector<float>>& M,int n,vector<vector<float>>& T, int n_thread,int n_block){
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