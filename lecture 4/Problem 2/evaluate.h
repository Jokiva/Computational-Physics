#pragma once
#include <iostream>
#include <fstream>
#include <string>
using namespace std;

// generate a linear space
// x[]: the array to be manipunated
// a: lower bound
// b: upper bound
// num: number in the linear space
template <typename T>
void linspace(T x[], T a, T b, int size) {
	// the step
	T step = (b - a) / (size - 1);
	// left end point
	x[0] = a;
	// right end point
	x[size - 1] = b;
	// inner points
	for (int i = 1; i < size - 1; i++) {
		x[i] = x[i - 1] + step;
	}
}

// calculate (x-1)^9 in different forms
// c: compact, e: expanded, h: horner
template <typename T>
void calc(T x[], T y[], const int size, char mode) {
	switch (mode) {
	case 'c': {// compact mode
			   // calculate (x-1)^9 directly
		for (int i = 0; i < size; i++) {
			y[i] = pow(x[i] - 1, 9);
		}
		break;
	}

	case 'e': {// expanded mode
			   // the expanded expression
		for (int i = 0; i < size; i++) {
			y[i] = -1 + 9 * x[i] - 36 * pow(x[i], 2) + 84 * pow(x[i], 3)
				- 126 * pow(x[i], 4) + 126 * pow(x[i], 5) - 84 * pow(x[i], 6)
				+ 36 * pow(x[i], 7) - 9 * pow(x[i], 8) + pow(x[i], 9);
		}
		break;
	}

	case 'h': {// Horner
			   // coefficients
		T coe[10]{ -1, 9, -36, 84, -126, 126, -84, 36, -9, 1 };
		// the sum
		/*T sum(coe[9] * x + coe[8]);
		for (int i = 7; i >= 0; i--)
		sum = sum * x + coe[i];*/
		for (int i = 0; i < size; i++) {
			T sum(coe[9] * x[i] + coe[8]);
			for (int j = 7; j >= 0; j--)
				sum = sum * x[i] + coe[j];
			y[i] = sum;
		}
		break;
	}
	default:
		cerr << "invalid evluation mode!" << endl;
	}
}

// print an array to console
template <typename T>
void pArr(const T arr[], int size) {
	for (int i = 0; i < size; i++) {
		cout << arr[i] << endl;
	}
}

// save an array to a file
template <typename T>
void sArr(const T arr[], int size, string name) {
	ofstream file(name + ".dat");
	for (int i = 0; i < size; i++) {
		file << arr[i] << endl;
	}
	file.close();
}

/*
// user defined power
template <typename T>
T pow(T base, int e) {
	prdct = 1;
	for (int i = 1; i < e; i++) {
		prdct *= base;
	}

	return prdct;
}*/
