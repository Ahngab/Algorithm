#include <stdio.h>
int main(void){
    int hour, minute, sum;
    
    scanf("%d %d", &hour, &minute);
    
    if (hour == 0) hour = 24;
    sum = hour * 60 + minute;
    sum -= 45;
    
    hour = sum / 60;
    minute = sum % 60;
    
    if (hour == 24) printf("0 %d", minute);
    else    printf("%d %d", hour, minute);
    return 0;
}