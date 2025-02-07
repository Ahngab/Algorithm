#include <stdio.h>
int main(void){
   int N, v, i, j, num = 0;
   int arr[100] = {0,};

   scanf("%d", &N);

   for(i = 0; i < N; i++){
      scanf("%d", &arr[i]);
   }
   scanf("%d", &v);

   for(j = 0; j < N; j ++) if (arr[j] == v) num++;
   printf("%d", num);
}