#ifndef FUNCTIONS_H
#define FUNCTIONS_H
#include <vector>
using namespace std;

void myFunctionS();
void myFunctionI();
void myFunctionO();

extern void (*matTranspose)(vector<vector<float>>& M,int n,vector<vector<float>>& T);
extern bool (*checkSym)(const vector<vector<float>>& M,int n);

#endif