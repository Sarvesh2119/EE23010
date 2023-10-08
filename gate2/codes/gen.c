#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <math.h>

int main() {
    // Seed the random number generator
    srand(time(NULL));

    // Number of samples
    int sample_size = 10000;

    // Generate X from an exponential distribution (exp(1))
    FILE *file_x = fopen("random_x.txt", "w");
    if (file_x == NULL) {
        fprintf(stderr, "Error opening file for X\n");
        return 1;
    }
    for (int i = 0; i < sample_size; i++) {
        double x = -log(rand() / (double)RAND_MAX);
        fprintf(file_x, "%lf\n", x);
    }
    fclose(file_x);

    return 0;
}

