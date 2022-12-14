#include<stdio.h>

int main(void){

	int n;
	
	scanf("%d", &n);
	
	int cent, vingt, dix, cinq;
	cent = n / 100;
	n -= cent*100;
	
	vingt = n / 20;
	n -= vingt*20;
	
	dix = n / 10;
	n -= dix*10;
	
	cinq = n / 5;
	n -= cinq*5;
	
	printf("%d\n", cent+vingt+dix+cinq+n);
	

	return 0;

}
