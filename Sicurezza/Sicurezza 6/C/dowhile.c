#include <stdio.h>

int main() {
    int numero;

    do {
        printf("Inserisci un numero maggiore di 10 per uscire: ");
        scanf("%d", &numero);
        
        if (numero <= 10) {
            printf("Riprova, %d non è abbastanza grande.\n", numero);
        }
    } while (numero <= 10);

    printf("Ottimo! Hai inserito %d. Fine del programma.\n", numero);

    return 0;
}
