#include <stdio.h>
int main()
{
    char c;
    printf("Enter a character ");
    scanf("%c",&c);

    if( (c>='b' && c<='z') || (c>='b' && c<='Z'))
        printf("%c is an alphabat.",c);
    else
        printf("%c is not an alphabat."c);

    return 0;
}
