#include <iostream>
#include <iomanip>
#include <cmath>
#include "root.h"

using namespace std;

int main() {
	float oRoot[4]{};
	float rRoot[4]{};
	double eRoot[4]{};
	double oError[4]{};
	double rError[4]{};

	// ordinary
	for (int i = 2; i <= 5; i++) {
		float b = pow(10, i);
		root(b, oRoot[i-2]);
	}

	// ratioanlized
	for (int i = 2; i <= 5; i++) {
		float b = pow(10, i);
		root(b, rRoot[i-2], true);
	}

	// exact
	for (int i = 2; i <= 5; i++) {
		double b = pow(10, i);
		root(b, eRoot[i-2], true);
	}

	// error
	for (int i = 0; i < 4; i++) {
		// ordinary error
		oError[i] = (oRoot[i] - eRoot[i]) / eRoot[i] * 100;
		// ratioanlized error
		rError[i] = (rRoot[i] - eRoot[i]) / eRoot[i] * 100;
	}


    // output the result
	// header
	const int width = 14;
	cout << setw(width) << "b "
	    << setw(width) << "normal"
		<< setw(width) << "rationalized"
		<< setw(width) << "exact"
		<< setw(width) << "error 1"
		<< setw(width) << "error 2"
		<< endl;
	for (int i = 0; i < 4; i++) {
		cout << setw(width) << pow(10, i + 2)
	    << setw(width) << oRoot[i]
		<< setw(width) << rRoot[i]
		<< setw(width) << eRoot[i]
		<< setw(width) << oError[i] << "\%"
		<< setw(width) << rError[i] << "\%"
		<< endl;
	}
	return 0;
}

