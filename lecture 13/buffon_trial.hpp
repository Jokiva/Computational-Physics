#pragma once
#include "shared_util.h"
#include <cmath>
#include <list>
using namespace std;


class BuffonNeedle {
protected:
	// length between lines
	const double line_int;
	// length of needle
	const double needle_length;

private:
	// the location of needle
	const double needle_loc;
	// angle of needle
	const double needle_angle;
	// if the trial is valid
	const bool valid;
	
public:
	BuffonNeedle(double li, double nl, double loc, double na)
		: line_int{ li }, needle_length{ nl }, needle_angle{ na }, needle_loc{loc}, valid{ needle_loc < needle_length * sin(needle_angle) / 2.0 } {
	}

	bool success(void) {
		return valid;
	}
};


class BuffonTrial {
private:
	// BuffonNeedle needle;
	list<BuffonNeedle*> trials;
	
	
	const size_t num_of_trials;
	// length between lines
	const double line_int;
	// length of needle
	const double needle_length;


public:
	BuffonTrial(double li, double nl, size_t nums)
		: line_int(li), needle_length{ nl }, num_of_trials{nums} {

		for (size_t i = 0; i < num_of_trials; ++i) {
			trials.push_back(new BuffonNeedle{ line_int, needle_length, uniform(0, line_int / 2), uniform(0, _Pi) });
		}
	}

	size_t count_case(void) {
		size_t valid_case = 0;
		// size_t total_case = 0;
		for (list<BuffonNeedle*>::const_iterator iter = trials.begin(); iter != trials.end(); ++iter) {
			if ((*iter)->success()) {
				++valid_case;
			}
		}

		return valid_case;
	}

	double sample_prob(void) {
		return (double)count_case() / (double)trials.size();
	}

	double calc_pi(void) {
		if (needle_length <= line_int) {
			return 2.0 / sample_prob() * needle_length / line_int;
		}
	}
};