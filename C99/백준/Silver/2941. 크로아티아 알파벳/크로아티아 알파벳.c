#include <stdio.h>
#include <string.h>
int main(void){
    char str[101];
    int i, cnt = 0;

    scanf("%s", str);

    cnt = strlen(str);
    for(i = 0; i < strlen(str); i++){
        if(str[i] == '-'){
            if (str[i-1] == 'c' || str[i-1] == 'd') cnt--;
        }
        else if(str[i] == '='){
            if(str[i-1] == 'c' || str[i-1] == 's') cnt--;
            if(str[i-1] == 'z' && str[i-2] == 'd') cnt -= 2;
            if(str[i-1] == 'z' && str[i-2] != 'd') cnt --;
        }
        else if(str[i] == 'j'){
            if(str[i-1] == 'n' || str[i-1] == 'l') cnt--;
        }
    }
    printf("%d", cnt);
    return 0;
}