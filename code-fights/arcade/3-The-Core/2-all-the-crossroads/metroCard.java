int[] metroCard(int lastNumberOfDays) {
  if (lastNumberOfDays == 28 || lastNumberOfDays == 30) {
    return new int[] {31};
  }
  return new int[] {28, 30, 31};
}
