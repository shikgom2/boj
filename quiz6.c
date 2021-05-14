#include <stdio.h>

int main(){
    int i,j;
    printf("중간 고사 점수를 입력하시오:");
    scanf("%d", &i);
    printf("기말고사 점수를 입력하시오:");
    scanf("%d", &j);

    if((i+j) / 2 >= 90)
    {
        printf("당신의 학점은 A학점입니다.\n");
    }
    else if((i+j) / 2 >= 80)
    {
        printf("당신의 학점은 B학점입니다.\n");
    }
    else if((i+j) / 2 >= 70)
    {
        printf("당신의 학점은 C학점입니다.\n");
    } 
    else if((i+j)/ 2 >= 60)
    {
        printf("당신의 학점은 D학점입니다.\n");
    }
    else{
        printf("당신의 학점은 F학점입니다.\n");
    }
    return 0;
}