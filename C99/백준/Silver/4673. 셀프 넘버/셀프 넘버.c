#include <stdio.h>
int sum(int n){
    int sum = n;

    while (n > 0){
        sum += n%10;
        n /= 10;
    }
    return sum;
}
int main(void){
    int arr[10001] = {0,};
    int i, j, dn;
    for(i = 0; i < 10001; i++){
        dn = sum(i);
        if (dn < 10001){
            arr[sum(i)] = 1;
        }
    }
    for(j = 0; j < 10001; j++){
        if (arr[j] == 0){
            printf("%d\n", j);
        }
    }
}