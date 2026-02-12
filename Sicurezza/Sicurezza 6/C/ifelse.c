# include <stdio.h>
int main(){
	int num;
	printf("Inserisci un numero:\n");
	scanf("%d",&num);
	if (num>5){
		printf ("Il numero %d e' maggiore di 5",num);
		}
	else {
		printf("Il numero %d  e' minore di 5",num);
		}
	return 0;
}
