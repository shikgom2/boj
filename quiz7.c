#include <stdio.h>
#include <math.h>

int main(){
    int a,b,c;

    printf("계수 a를 입력하시오 :");
    scanf("%d", &a);

    printf("계수 b를 입력하시오 :");
    scanf("%d", &b);

    printf("계수 c를 입력하시오 :");
    scanf("%d", &c);
    int tmp = b * b;
    int tmp2 = 4 * a * c * -1;

    if(a == 0)
    {
        printf("위의 이차 방정식의 근은 %.2f 입니다.\n", c * -1 / b);
    }
    else if(tmp - tmp2 < 0)
    {
        printf("위의 이차 방정식의 실근은 존재하지 않습니다.\n");
    }
    else{
        double val = (-b + (sqrt(b*b-4*a*c))) / (2 * a);
        double val2 = (-b - (sqrt(b*b-4*a*c))) / (2 * a);

        printf("위의 이차 방정식의 실근은 %.2f 과 %.2f 입니다.", val, val2);
    }
    return 0;
}