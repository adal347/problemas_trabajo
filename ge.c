#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char const *argv[]) {
    char palindrome[100];
    int i, j;
    printf("Give me a string\n");
    scanf("%s", palindrome);
    j = strlen(palindrome) - 1;
    for (i = 0; i < strlen(palindrome)/2; i++) {
        if (palindrome[i] != palindrome[j]) {
            printf("String [%s] is NOT a palindrome\n", palindrome);
            return 0;
        }
        j--;
    }
    printf("String [%s] is a palindrome\n", palindrome);
    return 0;
}
