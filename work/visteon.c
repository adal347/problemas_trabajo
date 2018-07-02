#include <stdio.h>

void swap(int *xp, int *yp) {
    int temp = *xp;
    *xp = *yp;
    *yp = temp;
}

void bubbleSort(int arr[], int n) {
   int i, j;
   for (i = 0; i < n-1; i++) {
       for (j = 0; j < n-i-1; j++) {
           if (arr[j] > arr[j+1]) {
               swap(&arr[j], &arr[j+1]);
           }
       }
   }
}

void printArray(int arr[], int size) {
    int i;
    for (i=0; i < size; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");
}

int main() {
    
    // Put your array here
    int arr[] = { 1, 7, 99, 2, 0, 12, 15 };

    int n = sizeof(arr)/sizeof(arr[0]);
    bubbleSort(arr, n);
    printf("Sorted array: \n");
    printArray(arr, n);

    return 0;
}
