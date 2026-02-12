#include <stdio.h>

int main() {
    int numero;

    do {
        printf("Inserisci un numero (maggiore di 10 per uscire, 0 per uscire subito): ");
        scanf("%d", &numero);

        
        if (numero == 0) {
            printf("Uscita d'emergenza attivata tramite break.\n");
            break; 
        }

        
        if (numero < 0) {
            printf("I numeri negativi non sono ammessi. Ricominciamo...\n");
            continue; 
            
        }

        if (numero <= 10) {
            printf("Riprova, %d non è abbastanza grande.\n", numero);
        }

    } while (numero <= 10);

    printf("Fine del programma. Valore finale: %d\n", numero);

    return 0;
}
