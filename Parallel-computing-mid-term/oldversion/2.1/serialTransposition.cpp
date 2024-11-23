#include "Functions.h"
#include <iostream>
#include <vector>
using namespace std;

void myFunctionS() {
    std::cout << "SERIAL Transposition" << std::endl;
}

vector<vector<float>> matTransposeSerial(const vector<vector<float>>& M){
    if (M.empty()) return {};

    vector<vector<float>> T(M[0].size(), vector<float>(M.size()));   // Create a new matrix with swapped dimensions T

    for (size_t i = 0; i < M.size(); ++i) {        // Use two nested loops to transpose the matrix
        for (size_t j = 0; j < M[0].size(); ++j) {
            T[j][i] = M[i][j];
        }
    }
    return T;
}