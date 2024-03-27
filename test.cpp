#include <iostream>

using namespace std;

int main() {
    int testcase;
    int height;
    int w;
    int room_number = 1;
    int height_number = 1;
    int room = 0;
    int sonnim;

    cin >> testcase;

    for (int i = 0; i < testcase; i++) {

        cin >> height >> w >> sonnim;  // 차례로 호텔의 높이, 층마다의 방 개수, 손님(몇 번째인지) 입력

        if (sonnim / height > 1) {  // 만약 손님이 호텔의 층 개수보다 많으면
            height_number = sonnim % height;  // 방 번호 (첫자리)는 손님을 층으로 나눈 값의 나머지이다. (6층 호텔의 10번째 손님은 4층에 있는 방)
            room_number = sonnim / height + 1;  // 방 번호 (끝자리)는 손님 / 층 + 1이다. (6층 호텔의 10번째 손님은 402호임)
        }

        else if (sonnim / height < 1) {  // 만약 손님이 호텔의 층 개수보다 적으면
            height_number = sonnim % height;
            room_number = 1;
        }

        else if (sonnim % height == 0) {  // 손님을 호텔의 층 개수로 나눴을 때 나머지가 0이면 꼭대기 층이다.
            height_number = height;
            room_number = sonnim / height;
        }
        room = height_number * 100 + room_number;
        cout << room << endl;
    }
}