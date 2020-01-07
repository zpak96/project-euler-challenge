
// # ProjectEuler100 challenge - Problem 1
// # Zane Paksi
//
// # Question:
// # If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
// # Find the sum of all the multiples of 3 or 5 below 1000.

#include <iostream>

using namespace std;

int main() {
  // Declaring sum here, and it will be added to when multiples are found below.
  int sum = 0;
  for (int i = 1; i < 1000; i++) {
    if (i % 3 == 0) {
      sum += i;
    } else if (i % 5 == 0) {
      sum += i;
    } // Once we're here, all multiples have been found and summed.
  }
  // printing to show answer.
  cout << sum << endl;
  return sum;
}
