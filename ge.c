#include <stdio.h>
#include <stdlib.h>

int main(int argc, char const *argv[]) {
    char* palindrome;
    int i, j;
    printf("Give me a string\n");
    scanf("%s", &palindrome);
    j = sizeof(palindrome);
    for (i = 0; i < sizeof(palindrome)/2; i++) {
        if (palindrome[i] != palindrome[j]) {
            printf("This string %s is not palindrome\n", palindrome);
            return 0;
        }
        printf("This string %s is palindrome\n", palindrome);
    }
    return 0;
}
