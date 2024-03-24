#include <iostream>
#include <string.h>

using namespace std;

int main() {
    char a[1000000];  // 문자열 a 선언
    int alphabet[26];  // 알파벳의 횟수 선언
    int index = 0;  // 알파벳 순서
    char character;  // 최대로 나온 알파벳
    bool question_mark = false;
    int max = -1; // 횟수의 최댓값

    cin >> a;  // 문자열 a를 입력받는다.

    int length = strlen(a);  // length는 입력받는 문자열의 길이

    for (int i = 0; i < length; i++) {   // a[0]부터 a[length]까지 저장된 알파벳을 소문자를 대문자로 변환시킴
        if ((int)a[i] > 96) {
            a[i] = a[i] - 32;
        }
    }

    for (int i = 0; i < length; i++) {  //alphabet 배열(횟수) 추가 시키기
        int result = a[i] - 65;
        alphabet[result] = alphabet[result] + 1;
    }
    
    for (int i = 0; i < 26; i++) {  // alphabet 배열 돌면서 최댓값 구하기
        if (alphabet[i] > max) {
            max = alphabet[i]; // 최대 빈도 수
            index = i;  // 그 알파벳의 순서
        }
    }

    int cnt = 0;
    for (int i = 0; i < 26; i++) {  // alphabet 배열 돌면서 최댓값 구하기
        if(alphabet[i] == max){
            cnt = cnt + 1;
        }
    }

    if(cnt >= 2){
        cout << '?' << endl;
    }
    else{
        cout << (char)(index + 65);
    }
}