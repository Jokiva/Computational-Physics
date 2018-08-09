#include <iostream>
#include <cmath>
#include <iomanip>

using namespace std;

double calcPi(unsigned long loops, char mode='f');
// double sumUp(int loops=5e5);
// double sumDown(int loops=5e5);

int main() {
    const unsigned long LOOPS = 5e5;
    // forward sum    
    double s1 = calcPi(LOOPS, 'f');
    double s2 = calcPi(LOOPS, 'b');
    double diff = s1 - s2;

    cout << "calculate in oridinary order:" << endl;
    cout << "s1=" << setprecision(50) << s1 << endl;
    cout << "calculate in inverse order:" << endl;
    cout << "s2=" << setprecision(50) << s2 << endl;
    cout << "the difference is " << setprecision(20) <<  diff << endl; 

    return 0;
}
/*
double sumUp(int loops) {
    double s = 0.0;
    double sign = 1;

    for (int i = 1; i < loops; i++) {
        s = s + sign / (2 * i - 1);
        sign = -sign;
    }

    return 4 * s;
}

double sumDown(int loops) {
    double s = 0.0;

    for (int i = loops; i > 0; i--)
        s += pow(-1, i - 1) / (2 * i - 1);

    return 4 * s;
}*/


// the template for calculate Pi
// loop is set to default by 500,000
// mode 'f' for forward, 'b' for backward
double calcPi(unsigned long loops, char mode) {
    double sum = 0.0;
    double sign = 0.0;
    
    switch (mode) {
        case 'f': 
            // the sign
            sign = 1;
            for (unsigned long n = 1; n <= loops; n++) {
                sum = sum + sign / (2 * n - 1);
                sign *= -1;
            }
            break;
        
        case 'b': 
            // the sign
            // +1 for odd n
            if (loops % 2 == 1)
                sign = 1;
            else
                sign = -1;
            // begin the summation
            for (unsigned long n = loops; n >= 1; n--) {
                sum = sum + sign / (2 * n - 1);
                sign *= -1;
            }
            break;
        
        default: 
            cerr << "invalid input!" << endl;
            exit(-1);
        
    }

    return 4 * sum;
}