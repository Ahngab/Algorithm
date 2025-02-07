#include <stdio.h>

int main(void){
    int C, N, i, j, k, cnt, sum;
    double avg;

    scanf("%d", &C);
    for(i = 0; i < C; i++){
        int scores[1000], sum = 0, cnt = 0;
        scanf("%d", &N);

        for(j = 0 ; j < N; j++){
            scanf("%d", &scores[j]);
            sum += scores[j];
        }

        avg = (double)sum / N;
        for(k = 0; k < N; k++){
            if (avg < scores[k]){
                cnt++;
            }
        }
        printf("%.3lf%%\n", (double)cnt * 100 / N);
    }
}