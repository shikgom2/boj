#include <stdio.h>
#include <stdbool.h>
int main(){
    
    int first, best, worst; //배치 기법 선택
    int size = 100;
    int data, n,i, j; //배치할 메모리, 배치기법 선택, for문에 사용될 i
    int idx;
    int k, temp;
    bool success;
    //기존 정보 복사

    printf("메모리 배치 기법별 메모리 배치\n");
    printf("여분의 메모리 공간의 개수를 입력하시오. (ex. [2, 55, 23, 65] = 4개) \n");
    scanf("%d", &size);
    int m[size]; //임의의 메모리 용량
    int mcopy[size];

    printf("각 메모리 용량을 입력하시오. \n");
    for(i=0; i<size; i++){
        scanf("%d", &m[i]);
    }

    printf("실행할 프로세스 용량을 입력하시오.\n");
    scanf("%d", &data);
    printf("배치기법을 선택하시오.\n");
    printf("1.First 2.Best 3.Worst \n");
    scanf("%d", &n);

    switch(n)
    {
        case 1:
            printf("최초 배치 기법에 따라 프로세스를 메모리에 배치합니다.\n");
            printf("현재 공백 상태인 메모리 :");
            for(i=0; i<size; i++){
                printf("%d ", m[i]);
            }
            printf("\n");
            
            //몇번째 메모리에 배치되는지 찾기
            //!추가 여기 부분은 이상해서 지우고 다시 짰습니다.
            for(i=0; i<size; i++){
                if( data <= m[i]){  //배치 성공
                    success = true;
                    printf("%d번째 메모리에 프로세스 배치\n", i+1);
                    printf("남은 메모리 :");
                    
                    m[i] -= data;   //배치 된 곳의 프로세스 용량 만큼 뺍니다
                    
                    for(j = 0; j< size; j++)
                    {
                        printf("%d ", m[j]);
                    }
                    printf("\n");
                    break;
                }
            }
            if(!success){
                //배치 실패
                printf("해당 프로세스를 배치할수 있는 메모리가 없습니다.\n");
            }
            break;

        case 2:
            printf("최적 배치 기법에 따라 프로세스를 메모리에 배치합니다.\n");
            printf("현재 공백 상태인 메모리 :");
            for(i=0; i<size; i++){
                printf("%d ", m[i]);
            }
            printf("\n");

            // 몇번째 메모리에 배치될지 찾기
            
            // mcopy에 m의 데이터를 저장 후, m메모리 공간을 오름차순으로
            for(i = 0; i<size; i++)
            {
                mcopy[i] = m[i];
            }
            for(k=0; k<size; k++){
                for(i=0; i<(size-1); i++){
                    if(m[i] > m[i+1]){
                        temp = m[i];
                        m[i] = m[i+1];
                        m[i+1] = temp;
                    }
                }
            }
            // m으로 최적적합 값을 찾고 idx에 저장
            for(i=0; i<size; i++){
                if(data<=m[i]){
                    idx = m[i];
                    break;
                }
            }

            //최적적합 값을 mcopy에서 찾기
            for(i=0; i<size; i++)
            {
                if(mcopy[i] == idx)
                {
                    success = true;
                    printf("%d번째 메모리에 프로세스 배치\n", i+1);
                                        
                    mcopy[i] -= data;   //배치 된 곳의 프로세스 용량 만큼 뺍니다
                    
                    printf("남은 메모리 : ");
                    for(j = 0; j< size; j++)
                    {
                        printf("%d ", mcopy[j]);
                    }
                    printf("\n");
                    break;
                }
            }

            if(!success){    
                //배치 실패
                printf("해당 프로세스를 배치할수 있는 메모리가 없습니다.\n");
            }
            break;

        case 3:
            printf("최악 배치 기법에 따라 프로세스를 메모리에 배치합니다.\n");
            printf("현재 공백 상태인 메모리 :");
            for(i=0; i<size; i++){
                printf("%d ", m[i]);
            }
            printf("\n");

            // 몇번째 메모리에 배치될지 찾기
            // mcopy에 m의 데이터를 저장 후, m메모리 공간을 오름차순으로
            for(i = 0; i<size; i++)
            {
                mcopy[i] = m[i];
            }
            // 메모리 공간을 내림차순으로
            for(k=size; k>0; k--){
                for(i=(size-1); i>0 ; i--){
                    if(m[i] > m[i-1]){
                        temp = m[i];
                        m[i] = m[i-1];
                        m[i-1] = temp;
                    }
                }
            }
            // m으로 최적적합 값을 찾고 idx에 저장
            for(i=0; i<size; i++){
                if(data<=m[i]){
                    idx = m[i];
                    break;
                }
            }

            //최적적합 값을 mcopy에서 찾기
            for(i=0; i<size; i++)
            {
                if(mcopy[i] == idx)
                {
                    success = true;
                    printf("%d번째 메모리에 프로세스 배치\n", i+1);
                                        
                    mcopy[i] -= data;   //배치 된 곳의 프로세스 용량 만큼 뺍니다
                    
                    printf("남은 메모리 : ");
                    for(j = 0; j< size; j++)
                    {
                        printf("%d ", mcopy[j]);
                    }
                    printf("\n");
                    break;
                }
            }

            if(!success){    
                //배치 실패
                printf("해당 프로세스를 배치할수 있는 메모리가 없습니다.\n");
            }
            break;

            
    default:
        printf("잘못 입력하셨습니다. 프로그램을 종료합니다.");
        break;
    }
    return 0;
}