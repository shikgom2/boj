#include <stdio.h>

int main(){
    int i,j,k;
    printf("삼각형의 세변을 입력하시오:");
    scanf("%d %d %d", &i, &j, &k);

    if(i == j && j == k)
    {
        printf("정삼각형\n");
    }
    else if(i == j || j == k || i == k)
    {
        printf("이등변삼각형\n");
    }
    else{
        printf("일반 삼각형\n");
    }
    return 0;
}