int phoneCall(int min1, int min2_10, int min11, int s) {
  int minutes = 0;
  if ((s - min1) >= 0) {
    s -= min1;
    minutes++;
  } else return 0;

  if (s - (min2_10 * 9) >= 0) {
    s -= (min2_10 * 9);
    minutes += 9;
  } else {
    return minutes + (s/min2_10);
  }

  return minutes + (s/min11);
}
