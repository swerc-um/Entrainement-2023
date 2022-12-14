#include <stdio.h>


int is_composite(int n){

	int i;
	int c = 0;
	for(i=1; i<=n; i++)
	{
		if(n % i == 0)
			c++;
	}
	if(c > 2)
		return 1;
	return 0;

}

int main(void) {
	
	int n;
 	scanf("%d", &n);
 	
 	int a = 2;
 	int b = a+n;
 	long i;
 	for(i = 0; i <= 1000000000; ++i){
 		
 		if (is_composite(a) && is_composite(b)) {
 			printf("%d %d\n", b, a);
 			break;
 		}
 		a++;
 		b++;
 	
 	}
 	
 	
	return 0;
}


