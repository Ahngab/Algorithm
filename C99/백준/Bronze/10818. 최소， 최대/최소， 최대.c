#include <stdio.h>

int main(void){
	int N,i,j;
	scanf("%d", &N);
	
	int array[N];
	for(i=0; i<N; i++){
		scanf("%d", &array[i]);
	}
	
	int max, min;
	max = array[0];
	min = array[0];
	
	
	for(j=0; j<N; j++){
		if (array[j] > max){
			max = array[j];
		}
		if (array[j] < min){
			min = array[j];
		}
	}
	
	printf("%d %d", min, max);
	return 0;	
}