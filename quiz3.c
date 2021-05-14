#include <stdio.h>

int main(){
    int i;
    printf("정수를 입력하시오:");
    scanf("%d", &i);

    if(i % 2 == 0)
    {
        printf("%d 은 짝수입니다\n", i);
    }
    else{
        printf("%d 은 홀수입니다\n", i);
    }
    return 0;
}