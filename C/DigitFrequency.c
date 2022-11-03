#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    int digits[10];
    char c;
    for(int i = 0; i < 10 ; i ++){
        digits[i] = 0;
    }
    while(scanf("%c",&c) == 1){
        if(c == '\n') break;
        if ((47 < (int)c) && ((int)c < 58)){
            digits[(int)c - 48]++;
        }
    }
    for(int i = 0; i < 10; i++){
        printf("%d ", digits[i]);
    }
    return 0;
}
