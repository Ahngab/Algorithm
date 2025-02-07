#include <stdio.h>
#include <string.h>
int main(void){
    int N, i, j, cnt = 0;

    scanf("%d", &N);
    for(i = 0; i < N; i++){
        char str[101];
        int alph[26] = {0,};

        scanf("%s", str);
        for(j = 0; j < strlen(str); j++){
            if(alph[str[j] - 'a'] == 0){
                alph[str[j] - 'a'] = 1;
            }
            else{
                if(str[j-1] != str[j]){
                break;
                }
            }

            if(j == strlen(str) - 1){
                cnt++;
            }
        }
    }
    printf("%d", cnt);
    return 0;
}