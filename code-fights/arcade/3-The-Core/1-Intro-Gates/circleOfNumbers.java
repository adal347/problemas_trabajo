int circleOfNumbers(int n, int firstNumber) {
  int index;

  if (firstNumber >= n/2) {
    index = firstNumber - (n/2);
  } else {
    index = firstNumber + (n/2);
  }

  return index;
}
