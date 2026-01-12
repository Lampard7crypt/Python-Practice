/* Program assignment for Lampard Kipyegon, SCT211-0049/2025. */
#include <stdio.h>
#include <stdlib.h>
#include <math.h>

// Calculates total marks
float calculateTotal(float marks[]) {
    float total = 0;
    for (int i = 0; i < 5; i ++) {
        total += marks[i];
    }
    return total;
}

// Calculates Average
float calculateAverage(float total) {
    return total/5.0;
}
/* Percentage is average with a modulo sign, that's why there's no calculatePercentage() function. */

int main() {
    printf("==Student Marks Calculation==\n");
    float total, avg, marks[5]; // Declare the float dtypes to be used.
    for (int i = 0; i < 5; i ++) {
        printf("Enter grade for subject %d: ",  i + 1);
        scanf("%f", &marks[i]);
    }
    total = calculateTotal(marks);
    avg = calculateAverage(total);
    printf("\n===Results===\n"); //Nice formatting of output.
    printf("Total: %.0f%\n", total);
    printf("Average: %.2f%\n", avg);
    printf("Percentage: %.2f%%", avg);
    printf("\n====End====\n");
    printf("Root %d is %.2f", 16, sqrt(16));
    return 0;
}