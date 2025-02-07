#include <stdio.h>
int main(void){
    int king, queen, rook, bisuope, night, phone;

    scanf("%d %d %d %d %d %d", &king, &queen, &rook, &bisuope, &night, &phone);
    printf("%d %d %d %d %d %d", 1 - king, 1 - queen, 2 - rook, 2 - bisuope, 2 - night, 8 - phone);
    return 0;
}
