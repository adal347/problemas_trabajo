int seatsInTheater(int nCols, int nRows, int col, int row) {
  int totalColumns = (nCols - col) + 1;
  int totalRows = nRows - row;
  return totalColumns * totalRows;
}
