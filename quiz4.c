#include <stdio.h>

int main(){
    char i;
    printf("신호등의 색깔 입력 (R,G,Y):");
    scanf("%c", &i);

    if(i == 'r' || i == 'R')
    {
        printf("정지!\n");
    }
    else if(i == 'G' || i == 'g'){
        printf("진행!\n");
    }
    else if(i == 'Y' || i == 'y')
    {
        printf("주의!\n");
    }
    return 0;
}