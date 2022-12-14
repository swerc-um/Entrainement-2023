#include<stdio.h>
#define SIZE 100000

int subset_sum(short B[], int n, int sum) {

	short table[n + 1][sum + 1]; 
	
	int i;
	int j;
	// si la somme vaut 0 alors vrai 
	for (i = 0; i <= n; i++) 
		table[i][0] = 1; 

	// si la somme attendue n'est pas 0 mais que le set est vide : false
	for (i = 1; i <= sum; i++) 
		table[0][i] = 0; 

	// DP : remplir la table
	for (i = 1; i <= n; i++) { 
		for (j = 1; j <= sum; j++) { 
			if (j < B[i - 1]) 
				table[i][j] = table[i - 1][j]; 
			if (j >= B[i - 1]) 
				table[i][j] = table[i - 1][j] || 
							table[i - 1][j - B[i - 1]]; 
		} 
	}
	return table[n][sum]; 
} 

int main(void){

	int t;
	scanf("%d", &t);
	
	short B[SIZE];
	int i;
	int n;
	int j;
	int s;
	for(i=0; i < t; ++i) {
		s=0;
		scanf("%d", &n);
		
		for(j=0; j < n; ++j) {
			scanf("%hu", &B[j]);
			s+=B[j];
		}
		
		if (((s % 2)==0) && subset_sum(B, n, s/2))
			printf("YES\n");
		else
			printf("NO\n");
	}

	return 0;

}
