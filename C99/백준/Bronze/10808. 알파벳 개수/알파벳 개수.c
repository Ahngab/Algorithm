#include <stdio.h>
#include <stdlib.h>

int main(){
    char str[100];
    int alph[26];
    
    scanf("%s", str);

    //Initialize alph as 0
    for(int i = 0; i < 26; i++){
        alph[i] = 0;
    }

    //Add str alphabet to alph
    for(int j = 0; j < strlen(str); j++){
        alph[str[j]-97]++;
    }

    //Print
    for(int k = 0; k < 26; k++){
        printf("%d ", alph[k]);
    }
    return 0;
}