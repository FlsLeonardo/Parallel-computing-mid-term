#ifndef FUNCTIONS_H
#define FUNCTIONS_H
#include <vector>
using namespace std;

void myFunctionS();
void myFunctionI();
void myFunctionO();
//vector<vector<float>> matTransposeSerial(vector<vector<float>> M,int n,vector<vector<float>> T);

extern void (*matTranspose)(vector<vector<float>>& M,int n,vector<vector<float>>& T, int n_thread,int n_block);
extern bool (*checkSym)(const vector<vector<float>>& M,int n, int n_thread);

#endif