#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_LENGTH 255

struct vparameter{  //구조체 선언
    int vseq;
    char vkey[10];
    char vpvalue[30];
};

int lastIndex = 0;  //전체 등록 갯수

//함수 원형 선언
void addTitle();
void loadParameter();
void addSubTitle();
void initData();
void mainLoop();
void modifyData();
void deleteData();
void printFront();
void printBack();

//시작 제목 출력 함수
void addTitle(){
    printf("%-5s%-10s%s\n", "seq", "parameter", "parameter value");
    printf("------------------------------\n");
}

void loadParameter(){   //전체 출력 함수
    FILE* file = fopen("setupfile.txt", "rt");  //setupfile.txt 파일을 엽니다
    char buffer[MAX_LENGTH];
    lastIndex = 0;
    while(fgets(buffer, MAX_LENGTH, file) != NULL)	//1줄씩 읽어옴
    {
        printf("%s", buffer);	//그대로 1줄 출력
        lastIndex ++;   //전체 등록 갯수 출력
    }
    fclose(file);
    printf("\n");
}

//각종 기능 switch 함수
void addSubTitle(){
    printf("------------------------------\n");
    printf("1. 입력 2. 수정 4. 삭제 7. 앞으로 8. 뒤로 9. 종료 \n원하는 작업을 선택하세요 : ");
    int i;

    scanf("%d", &i);

    switch(i){
        case 1:
            initData();
            break;
        case 2:
            modifyData();
            break;
        case 4:
            deleteData();
        case 7:
            printFront();
            break;
        case 8:
            printBack();
            break;
        case 9:
            printf("프로그램을 종료합니다.\n");
            break;
        default:
            printf("유효한 숫자가 아닙니다.");
            break;
    }
}

void initData(){//데이터 입력
    struct vparameter vp;   //위 정의한 구조체 변수 선언
    printf("------------------------------\n");
    printf("Parameter을 입력하세요 : ");
    scanf("%s", vp.vkey);

    printf("Parameter value를 입력하세요 : ");
    scanf("%s", vp.vpvalue);

    lastIndex++;	//전체 저장갯수 1 증가
    vp.vseq = lastIndex;	//인덱스 자동 지정

    FILE* file = fopen("setupfile.txt", "a+");  //저장되어있는 파이을 엽니다.
    fprintf(file, "%-4d%-10s%-30s\n", vp.vseq, vp.vkey, vp.vpvalue);	//구조체 내에 저장한 변수들을 txt 형식에 맞게 저장

    printf("입력이 완료되었습니다.\n");
    fclose(file);
    
    mainLoop();
}

void modifyData(){  //데이터 수정
    struct vparameter vp;  
    printf("------------------------------\n");
    printf("수정할 Seq번호를 입력하세요 : ");
    scanf("%d", &vp.vseq);
    
    printf("수정할 Parameter을 입력하세요 : ");
    scanf("%s", vp.vkey);

    printf("수정할 Parameter value를 입력하세요 : ");
    scanf("%s", vp.vpvalue);

    FILE* file = fopen("setupfile.txt", "r+");
    fseek(file, (sizeof(vp) * vp.vseq) - sizeof(vp), SEEK_CUR);     //txt파일의 해당 seq번호를 가지고 있는 인덱스의 해당 위치를 찾기
    fprintf(file, "\n%-4d%-10s%-30s", vp.vseq, vp.vkey, vp.vpvalue); 	//위치에서 수정
    rewind(file);	//fseek로 파일 인덱스를 변경한걸 처음으로 되돌려줍니다.

    printf("수정이 완료되었습니다.\n");

    fclose(file);
    mainLoop();
}

void deleteData(){  //데이터 삭제 
    struct vparameter vp;
    printf("------------------------------\n");
    printf("삭제할 Seq번호를 입력하세요 : ");
    scanf("%d", &vp.vseq);

    //삭제는 file2에 삭제할것을 제외하고 복사를 한뒤에 기존 file1을 지우고 file2를 file1로 이름을 바꿔서 합니다.
    FILE* file = fopen("setupfile.txt", "rt");
    FILE* file2 = fopen("setupfile2.txt", "a+");
 
    char buffer[MAX_LENGTH];
    char tmp[MAX_LENGTH];
    int dataCount = 0;

    while(fgets(buffer, MAX_LENGTH, file) != NULL)	//1줄씩 읽음
    {
        if(buffer[0] == vp.vseq + '0')	//삭제 인덱스 확인
        {
            //delete index do nothing
        }
        else{
            dataCount++;
            buffer[0] = dataCount + '0';	//dataCount는 새로운 일렬번호, buffer형은 char형이라 '0'을 추가해 int형을 char형으로 바꿉니다.
            fprintf(file2, buffer);	//file2에 1줄 읽어옴
        }
    }
    lastIndex -=1;
    fclose(file);
    fclose(file2);
    remove("setupfile.txt");	//기존 파일 제거
    rename("setupfile2.txt", "setupfile.txt");	//새로운 파일 기존파일명으로 변경

    printf("\n");
    rewind(file);

    printf("삭제가 완료되었습니다.\n");

    fclose(file);
    mainLoop();
}

//print front 5
void printFront(){
    addTitle();
    FILE* file = fopen("setupfile.txt", "rt");  //setupfile.txt 파일을 엽니다.
    char buffer[MAX_LENGTH];
    int count = 0;  //몇개 읽었는지 저장하는 변수
    while(fgets(buffer, MAX_LENGTH, file) != NULL)	//1줄씩 읽음
    {
        count ++;
        printf("%s", buffer);
        if(count >= 5)	//전체 갯수에서 앞에서 5개까지만 출력
        {
            break;
        }
    }
    fclose(file);
    printf("\n");

    addSubTitle();
}

//print back 5 
void printBack(){
    addTitle();
    FILE* file = fopen("setupfile.txt", "rt");  //setfile.txt 파일을 엽니다
    char buffer[MAX_LENGTH];
    int printIndex = 0;
    while(fgets(buffer, MAX_LENGTH, file) != NULL)	//1줄씩 읽음
    {
        printIndex ++;

        if(lastIndex - 5 < printIndex)	//전체 갯수에서 뒤에서 5개만 출력
        {
            printf("%s", buffer);
        }
    }
    fclose(file);
    printf("\n");
    addSubTitle();
}
void mainLoop(){
    addTitle();
    loadParameter();
    addSubTitle();
}

int main(){
    mainLoop();
}