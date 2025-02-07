#include <stdio.h>

int main(void){
	int i, j, max, N;
	int array[9];
	
	for(i=0; i<10; i++){
		scanf("%d", &array[i]);
	}
	
	max = array[0];
	N = 0;
	for(j=0; j<10; j++){
		if (array[j] > max){
			max = array[j];
			N = j;
		}
	}
	printf("%d\n", max);
	printf("%d", N+1);

}