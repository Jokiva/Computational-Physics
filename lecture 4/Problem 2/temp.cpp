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
void linspace(T x[], T a, T b, int num) {
	// the step
	T step = (b - a) / (num - 1);
	// left end point
	x[0] = a;
	// right end point
	x[num - 1] = b;
	// inner points
	for (int i = 1; i < num - 1; i++) {
		x[i] = x[i - 1] + step;
	}
}

// print an array to console
template <typename T>
void pArr(T arr[], int size) {
	for (int i = 0; i < size; i++) {
		cout << arr[i] << endl;
	}
}

// save an array to a file
template <typename T>
void sArr(T arr[], int size, string name) {
	ofstream file(name + ".dat");
	for (int i = 0; i < size; i++) {
		file << arr[i] << endl;
	}
	file.close();
}
