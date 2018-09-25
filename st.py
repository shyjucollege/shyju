#include <string.h>
#include <stdio.h>
 
int main(int argc, char* argv[]) {
    if(strspn(argv[1], "0123456789.") == strlen(argv[1])) {
        printf("The string has only numbers and '.'!");
    } else {
        printf("The string has characters that are not numbers or period!");
    }
 
    return 0;
}
