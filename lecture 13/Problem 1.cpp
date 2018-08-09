#include "shared_util.h"
#include "buffon_trial.hpp"
#include <iostream>
#include <vector>
using namespace std;


// debug mode selection
#ifndef DEBUG
	#define DEBUG 1
#endif // !DEBUG



int main() {
#if DEBUG
	try {
		// 
		vector<double> arr = linspace(1.0, 2.0, 2);
		print_vec(arr);

		cout << "\nrandom number demo in c++11" << endl;
		std::random_device generator;
		uniform_real_distribution<double> ran(0, 5);
		for (size_t i = 0; i < 10; ++i) {
			cout << ran(generator) << endl;
		}

		cout << "\nmy uniform distrubution generator: " << endl;
		for (size_t i = 0; i < 10; ++i) {
			cout << uniform(0, 5) << endl;
		}

		cout << "\nbuffon needle demo" << endl;
		BuffonTrial trial{ 1, 1, 10000 };
		cout << trial.calc_pi() << endl;
	}

	catch (const std::exception& exp) {
		cout << endl << "exception caught: "
			<< exp.what();
	}
#endif // DEBUG
	system("pause");
	return 0;
}