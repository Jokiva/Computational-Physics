#pragma once
#include <vector>
#include <iostream>
#include <cstdlib>
#include <cmath>
#include <ctime>
#include <random>
using namespace std;


// this function createa a matlab-like linspace
// a: the lower bound of interval
// b: the upper bound of interval
// num: the number of panels in the interval
vector<double> linspace(double a, double b, size_t num) {
	if (b <= a) {
		throw runtime_error("the length of interval must be greater than zero");
	}

	double h = (b - a) / (double)num;

	// create the interval
	vector<double> arr(num + 1);
	for (size_t i = 0; i < arr.size(); ++i) {
		arr[i] = a + i * h;
	}
	arr[arr.size() - 1] = b;

	return arr;
}

// this function outputs a vector in a column, the default ostream is cout
template <typename T>
int print_vec(const vector<T>& arr, ostream& output=cout) {
	for (typename vector<T>::const_iterator iter = arr.begin(); iter != arr.end(); ++iter) {
		output << *iter << endl;
	}

	return 0;
}

#pragma region RANDOM_NUMBER_UNIT
// typedefs
typedef random_device RandomGenerator;
typedef uniform_real_distribution<double> UniRand;

// shared random number generator, default is random device
static RandomGenerator seed;

// this fucntion sets the seed of random number generetor
inline size_t set_seed(size_t s) {
	// srand(s);
	

	return 0;
}

// this fuction returns a uniformly distributed random number
// on instruccted interval [a, b]
inline double uniform(double a, double b) {
	if (b <= a) {
		throw runtime_error("the length of interval must be greater than zero");
	}

	UniRand ran(a, b);
	return ran(seed);
}
#pragma endregion

