#include <cmath>
#include <iostream>
#include <quadmath.h>
__float128 artan(__float128 x, __float128 loops=5e55);
__float128 calcPi();

// standard PI in mathematica
const __float128 PI = 3.14159265358979323846264338327950288419716939937510582097494459230781\
6406286208998628034825342117068q;

int main()
{
    // calculate pi using machin formula
    // __float128 precision
    __float128 pi = calcPi();
    __float128 diff = pi - PI;
    printf ("calculated pi:\n%.100Qe\n", pi);
    printf ("standard pi in matheamtica:\n%.100Qe\n", PI);
    printf ("the difference:\n%.100Qe\n", diff);

    
	return 0;
}

__float128 artan(__float128 x, __float128 loops) {
	__float128 sum(0.0q);
    // __float128 sign(0.0q);

    // initial sign
    // positive if n is odd
    /*
    if (loops % 2 == 1)
        sign = 1;
    else
        sign = -1
    */ 
	for (__float128 i = loops; i >= 1; i--) {
		sum += powq(-1, i - 1) * powq(x, 2 * i - 1) / (2 * i - 1);
	}

	return sum;
}

__float128 calcPi(){
    __float128 a = 1.0q;
    __float128 b = 1.0q;

    a = a / 5;
    b = b / 239;
    return 4 * (4 * atanq(a) - atanq(b));
    // return 4 * (4 * artan(a) - artan(b));
}