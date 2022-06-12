#include <stdio.h>

int main() {
    float yield;
    float startsum;
    int period;
    int i;
    float cal;

    printf_s("Enter the starting sum:\n");
    scanf_s("%f", &startsum);
    printf_s("Enter the yield:\n");
    scanf_s("%f", &yield);
    printf_s("Enter the period:\n ");
    scanf_s("%d", &period);

    for(i = 0; i < period; i++){
       cal = startsum + (startsum * (yield / 100));
       startsum = cal;
 }

    printf_s("Total earned for the period is: ", cal);
    printf_s("%.2f\n", cal);
}

//do a calculator for APY.