#include <stdio.h>

int main() {
    int a, b;
    printf("Inserisci due numeri:\n");
    
    
    scanf("%d %d", &a, &b); 

    if (a == b) {
        
        printf("i due numeri sono uguali\n %d %d", a, b);
    }
    else {
        
        printf("i due numeri non sono uguali\n %d %d", a, b);
    }
    return 0;
}