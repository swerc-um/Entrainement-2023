#include<stdio.h>

#define CONTEST_TIME 240

int main(void){

	int n, k;
	
	scanf("%d %d", &n, &k);
	int max_time =  (CONTEST_TIME - k) / 5;
	
	int d=0;
	int f=n;
	int m;
	int c;
	while (d <= f) {
		m = (f+d)/2;
		c = (m*(m+1)/2);
		if (c < max_time)
			d=m+1;
		else if (c==max_time)
			break;
		else
			f=m-1;
	}
	m = (f+d)/2;
	printf("%d\n", m);

	return 0;

}
