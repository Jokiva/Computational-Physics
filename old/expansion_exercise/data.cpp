#include "iostream"
#include "cmath"
#include "fstream"
#include "iomanip"

using namespace std;
// create four .txt file to store the value
ofstream x_out ("x.txt");
ofstream y1_out ("y1.txt");
ofstream y2_out ("y2.txt");
ofstream error_out ("error.txt");

// declare four functions to compute the value
void x(double l, double u);
void y1(double l, double u);
void y2(double l, double u);
void error(double l, double u);

// set precision of the output value
int main(int argc, char const *argv[]) {
  x_out << fixed << setprecision(7);
  y1_out << fixed << setprecision(20);
  y2_out << fixed << setprecision(20);
  error_out << fixed << setprecision(20);

  x(0.99, 1.01); // compute the functions' value on [0.99, 1.01]
  y1(0.99, 1.01);
  y2(0.99, 1.01);
  error(0.99, 1.01);

  return 0;
}


// details of the functions, length of the step is 0.000001
// create the domain of plotting
void x(double l, double u) {
  for (double i = l; i <= u; i += 0.00001) {
    x_out << i << endl;
  }
}

// (x-1)^7 is expanded in y1 to compute
void y1(double l, double u) {
  for (double i = l; i <= u; i += 0.00001) {
    y1_out << pow(i, 7) - 7 * pow(i, 6) + 21 * pow(i, 5) - 35 * pow(i, 4) + 35 * pow(i, 3) - 21 * pow(i, 2) + 7 * i - 1 << endl;
  }
}

// (x-1)^7
void y2(double l, double u) {
  for (double i = l; i <= u; i += 0.00001) {
    y2_out << pow((i - 1), 7) << endl;
  }
}

// relative error
void error(double l, double u) {
  for (double i = l; i <= u; i += 0.00001) {
    error_out << abs((pow(i, 7) - 7 * pow(i, 6) + 21 * pow(i, 5) - 35 * pow(i, 4) + 35 * pow(i, 3) - 21 * pow(i, 2) + 7 * i - 1) - (pow((i - 1), 7)))/ abs(pow((i - 1), 7)) << endl;
  }
}
