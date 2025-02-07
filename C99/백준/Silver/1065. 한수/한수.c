#include <stdio.h>

int main(void){
    int num, res;
    scanf("%d", &num);

    res = Hans(num);
    printf("%d", res);
}

int Hans(int num){
    int hund, ten, one, i, cnt = 0;
    if (num < 100) return num;
    
    else{
        for (i = 100; i <= num; i++){
            hund = i / 100;
            ten = (i % 100) / 10;
            one = (i) - (hund*100) - (ten*10);
            if( hund - ten == ten - one) cnt++;
        }
        return (cnt + 99);
    }
}