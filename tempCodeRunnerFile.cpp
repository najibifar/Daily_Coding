#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <omp.h>

int main() {
    const int N = 100000000;
    int *X = malloc(N * sizeof(int));
    int *Y = malloc(N * sizeof(int));
    int *Z = malloc(N * sizeof(int));

    for (int i = 0; i < N; i++) {
        X[i] = i;
        Y[i] = i;
    }

    double t1 = omp_get_wtime();

    omp_set_num_threads(2);   // استفاده از ۶ هسته CPU
    #pragma omp parallel for
    for (int i = 0; i < N; i++) {
        Z[i] = X[i] + Y[i];
    }

    double t2 = omp_get_wtime();
    printf("Time: %f seconds\n", t2 - t1);

    free(X);
    free(Y);
    free(Z);
    return 0;
}

