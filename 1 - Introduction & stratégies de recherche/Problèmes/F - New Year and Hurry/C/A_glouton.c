#include<stdio.h>

#define CONTEST_TIME 240

int main(void){

	int n, k;
	
	scanf("%d %d", &n, &k);
	int max_time =  CONTEST_TIME - k;
	int c=0;
	int cur_t=0;
	while ((c < n) && ((c+1)*5+cur_t <= max_time)) {
		c++;
		cur_t+=5*c;
	}
	
	printf("%d\n", c);

	return 0;

}
