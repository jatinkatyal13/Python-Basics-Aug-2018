#include <stdio.h>

int main() {
    while (1) {
        int x;
        scanf("%d", &x);
        if (x == 42) break;
        printf("%d\n", x);
    }
    
    return 0;
}