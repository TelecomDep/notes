#include <stdio.h>
#define SIZE 10000

int arr[SIZE][SIZE]; 

int main() {
    long long sum = 0;

    for (int i = 0; i < SIZE; i++) {
        for (int j = 0; j < SIZE; j++) {
            sum += arr[i][j]; 
        }
    }
    return 0;
}