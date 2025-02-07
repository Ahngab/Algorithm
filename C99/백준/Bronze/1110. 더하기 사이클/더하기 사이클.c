#include <stdio.h>
int cal(int a){
    int first, second;
    first  = a / 10;
    second = a%10;
    return ((second * 10) + ((first + second) % 10));
}

int main(void){
    int N, val, cnt = 1;

    scanf("%d", &N);
    if (N <= 9) N *= 10;
    
    val = cal(N);
    val = cal(N);

    while (1){
        if (N == val) break;
        else {cnt += 1;
        val = cal(val);
        }
    }

    printf("%d", cnt);
}