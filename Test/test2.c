#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>



int main()
{
    int a, b, c, d, i, j;
    scanf("%d\n%d", &a, &b);
      // Complete the code.
   //printf("%d\n%d", a, b);
    if (a <= 9){
        for (i = a; i <= 9; i++){
            if (i <= 9){
                if (i == 1) {
                printf("one");
                }
                else if (i == 2){
                printf("two");
                }
                else if (i == 3) {
                printf("three");
                }
                else if (i == 4) {
                printf("four");
                }
                else if (i == 5) {
                printf("five");
                }
                else if (i == 6) {
                printf("six");
                }
                else if (i == 7) {
                printf("seven");
                }
                else if (i == 8) {
                printf("eight");
                }
                else {
                printf("nine");
                }
                printf("\n");
            }
            //printf("\n");
        }
        c = a % 2;
                if (c == 0){
                    printf("even");
                }
                else {
                    printf("odd");
       }
    }
    else{
        c = a % 2;
                if (c == 0){
                    printf("\nev");
                }
                else {
                    printf("\nodd");
                }
    }
    //program for b
    if (b <= 9){
        for (j = b; j <= 9; j++){
            if (j <= 9){
                if (j == 1) {
                printf("\none");
                }
                else if (j == 2){
                printf("\ntwo");
                }
                else if (j == 3) {
                printf("\nthree");
                }
                else if (j == 4) {
                printf("\nfour");
                }
                else if (j == 5) {
                printf("\nfive");
                }
                else if (j == 6) {
                printf("\nsix");
                }
                else if (j == 7) {
                printf("\nseven");
                }
                else if (j == 8) {
                printf("\neight");
                }
                else {
                printf("\nnine");
                }
            }
        }
        d = b % 2;
                if (d == 0){
                    printf("\neven");
                }
                else {
                    printf("\nodd");
                }
    }
    else{
        d = b % 2;
                if (d == 0){
                    printf("\neven");
                }
                else {
                    printf("\nodd");
                }
    }
    return 0;
}
