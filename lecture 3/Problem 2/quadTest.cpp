#include <iostream>
#include <cmath>
#include <iomanip>

typedef __float80 quad;

quad atan(quad , int);

int main() {
  // quad x = 0;
  // std::cout << x << std::endl;
  const int NUM = 20;
  // quadratic
  std::cout << "quadratic" << std::endl;
  quad a1 = 0.2, b1 = 1.0 / 239;
  quad s1 = 4 * atan(a1) - atan(b1);
  
  std::cout << std::setprecision(NUM) << s1 << std::endl;
  

  // double
  std::cout << "double" << std::endl;
  double a2 = 0.2, b2 = 1.0 / 239;
  double s2 = 4 * atan(a2) - atan(b2);
  
  std::cout << std::setprecision(NUM) << s2 << std::endl;

  return 0;
}

quad atan(quad x, int loops=5e7) {
  quad s = 0;
  
  for (int n = loops; n > 0; n--)
      // s += (-1) ^ (n-1) * x ^ (2 * n - 1) / (2 * n - 1);
      s += pow(-1, n-1) * pow(x, 2 * n - 1) / (2 * n - 1);

  return s;
}

double atan(double x, int loops=5e7) {
  double s = 0;
  
  for (int n = loops; n > 0; n--)
      // s += (-1) ^ (n-1) * x ^ (2 * n - 1) / (2 * n - 1);
      s += pow(-1, n-1) * pow(x, 2 * n - 1) / (2 * n - 1);

  return s;
}