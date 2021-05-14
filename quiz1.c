#include <stdio.h>

int main(){
    int i,j;
    printf("정수를 입력하시오:");
    scanf("%d", &i);
    printf("정수를 입력하시오.");
    scanf("%d", &j);


    printf("두수의 합은 %d입니다.\n",i+j);

    if(i>=j)
    {
        printf("두수의 차는 %d입니다.\n", i-j);
    }
    else{
        printf("두수의 차는 %d입니다.\n", j-i);
    }
    return 0;
}