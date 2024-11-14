#ifndef FUNCTIONS_H
#define FUNCTIONS_H
#include <vector>
using namespace std;

void myFunctionS();
void myFunctionI();
void myFunctionO();

extern vector<vector<float>> (*matTranspose)(const vector<vector<float>>& M);
extern vector<vector<float>> (*matSymmmetry)(const vector<vector<float>>& M);

#endif