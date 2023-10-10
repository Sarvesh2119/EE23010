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
    FILE *file_x_w = fopen("random_x.txt", "w");
    if (file_x_w == NULL) {
        fprintf(stderr, "Error opening file for X\n");
        return 1;
    }
    for (int i = 0; i < sample_size; i++) {
        double x = -log(rand() / (double)RAND_MAX);
        fprintf(file_x_w, "%lf\n", x);
    }
    fclose(file_x_w);

FILE *file_x = fopen("random_x.txt", "r"); // Open in read mode
    if (file_x == NULL) {
        fprintf(stderr, "Error opening file for X\n");
        return 1;
    }

    // Generate Y = e^(-X)
    FILE *file_e_minus_X = fopen("e_minus_X.txt", "w");
    if (file_e_minus_X == NULL) {
        fprintf(stderr, "Error opening file for e^(-X)\n");
        fclose(file_x); // Close the file
        return 1;
    }

    // Generate 1 - e^(-X)
    FILE *file_one_minus_e_minus_X = fopen("one_minus_e_minus_X.txt", "w");
    if (file_one_minus_e_minus_X == NULL) {
        fprintf(stderr, "Error opening file for 1 - e^(-X)\n");
        fclose(file_x); // Close the file
        fclose(file_e_minus_X); // Close the file
        return 1;
    }

    // Generate 2e^(-X) - 1
    FILE *file_two_e_minus_X_minus_1 = fopen("two_e_minus_X_minus_1.txt", "w");
    if (file_two_e_minus_X_minus_1 == NULL) {
        fprintf(stderr, "Error opening file for 2e^(-X) - 1\n");
        fclose(file_x); // Close the file
        fclose(file_e_minus_X); // Close the file
        fclose(file_one_minus_e_minus_X); // Close the file
        return 1;
    }

    // Generate a sample of random numbers from a uniform distribution between -1 and 1
    FILE *file_uniform_minus_1_to_1 = fopen("uniform_minus_1_to_1.txt", "w");
    if (file_uniform_minus_1_to_1 == NULL) {
        fprintf(stderr, "Error opening file for Uniform (-1 to 1)\n");
        fclose(file_x); // Close the file
        fclose(file_e_minus_X); // Close the file
        fclose(file_one_minus_e_minus_X); // Close the file
        fclose(file_two_e_minus_X_minus_1); // Close the file
        return 1;
    }

    // Generate a sample of random numbers from a uniform distribution between 0 and 1
    FILE *file_uniform_0_to_1 = fopen("uniform_0_to_1.txt", "w");
    if (file_uniform_0_to_1 == NULL) {
        fprintf(stderr, "Error opening file for Uniform (0 to 1)\n");
        fclose(file_x); // Close the file
        fclose(file_e_minus_X); // Close the file
        fclose(file_one_minus_e_minus_X); // Close the file
        fclose(file_two_e_minus_X_minus_1); // Close the file
        fclose(file_uniform_minus_1_to_1); // Close the file
        return 1;
    }

    for (int i = 0; i < sample_size; i++) {
        double x;
        fscanf(file_x, "%lf", &x);
        
        // Calculate Y = e^(-X) and write to file
        double y = exp(-x);
        fprintf(file_e_minus_X, "%lf\n", y);

        // Calculate 1 - e^(-X) and write to file
        double one_minus_e_minus_x = 1 - exp(-x);
        fprintf(file_one_minus_e_minus_X, "%lf\n", one_minus_e_minus_x);

        // Calculate 2e^(-X) - 1 and write to file
        double two_e_minus_x_minus_1 = 2 * exp(-x) - 1;
        fprintf(file_two_e_minus_X_minus_1, "%lf\n", two_e_minus_x_minus_1);

        // Generate a sample of random numbers from a uniform distribution between -1 and 1 and write to file
        double u_minus_1_to_1 = -1.0 + 2.0 * ((double)rand() / (double)RAND_MAX);
        fprintf(file_uniform_minus_1_to_1, "%lf\n", u_minus_1_to_1);

        // Generate a sample of random numbers from a uniform distribution between 0 and 1 and write to file
        double u_0_to_1 = (double)rand() / (double)RAND_MAX;
        fprintf(file_uniform_0_to_1, "%lf\n", u_0_to_1);
    }

    // Close all files
    fclose(file_x);
    fclose(file_e_minus_X);
    fclose(file_one_minus_e_minus_X);
    fclose(file_two_e_minus_X_minus_1);
    fclose(file_uniform_minus_1_to_1);
    fclose(file_uniform_0_to_1);
    return 0;
}

