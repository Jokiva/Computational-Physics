#pragma once
// the function evaluate the roots
// and store them in a certain array
template <typename T>
void root(const T b, T& arr, const bool normalize=false) {
	if (!normalize) {
		double r = sqrt(b * b - 4);
		// arr[0] = (b + r) / 2;
		arr = (b - r) / 2;
	}

	else {
		T r = sqrt(b * b - 4);
		// arr[0] = (b + r) / 2;
		arr =  2 / (b + r);
	}
}