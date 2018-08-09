#include <iostream>
#include <fstream>
#include <string>
#include <cmath>
#include "evaluate.h"
using namespace std;


int main()
{
	// the size of the array
    // also can be interpreted as the number of steps
    // in the invertal
	const int size =10001;
    // different modes
    const int types = 3;
	char modes[types]{'c', 'e', 'h'};


	// first evaluate the expression in float
	// init
	float* x1 = new float[size];
	float* y1 = new float[size];
	linspace(x1, (float)0.7, (float)1.3, size);
    // store x1 in "x1.dat"
    sArr(x1, size, "x1");
    // for dofferent types of algorithm
    // evaluate the expression
    // store them in corresponding file
    for (int i = 0; i< types; i++) {
        calc(x1, y1, size, modes[i]);
        sArr(y1, size, "y1"+to_string(i));
    }
    // reclaim space
    delete[] x1;
    delete[] y1;
    
    
    // evaluate the expression in double
	// init
	double* x2 = new double[size];
	double* y2 = new double[size];
	linspace(x2, (double)0.7, (double)1.3, size);
    // store x2 in "x2.dat"
    sArr(x2, size, "x2");
    // for dofferent types of algorithm
    // evaluate the expression
    // store them in corresponding file
    for (int i = 0; i< types; i++) {
        calc(x2, y2, size, modes[i]);
        sArr(y2, size, "y2"+to_string(i));
    }
    // reclaim space
    delete[] x2;
    delete[] y2;

    return 0;
}
