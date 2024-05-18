#include <iostream>
#include <vector>
#include <cstring>

using namespace std;

int map[1001][1001];  // 맵 구성
int visit[1001][1001];  // 칸마다 방문여부 확인용

int dx[4] = {0,0,1,-1};  // 4방향 확인을 위한 배열 (양 옆 확인)
int dy[4] = {1,-1,0,0};  // 4방향 확인을 위한 배열 (위 아래 확인)

int m, n;  // m, n 값
bool ans = false;  // 맨 아래까지 도달할 수 있는 지 여부

void dfs(int x, int y)  // DFS 함수
{
    cout << x << " " <<  y << "\n";

    visit[x][y] = 1;  // 시작 부분을 1로 변경

    for (int i = 0; i < 4; i++)  // 4방향 확인
    {
        int tx = x + dx[i];
        int ty = y + dy[i];

        if(tx == n-1){
            ans = true;
            return;
        }

        if(0 <= tx && tx < m && 0 <= ty && ty < n)  // 범위 내 일때
        {
            if (map[tx][ty] == 0 && visit[tx][ty] == 0)  // 갈 수 있는 칸일때(전기가 통할 때)
            {
                dfs(tx, ty);  // 다음 칸으로 DFS 반복
                if (ans) return;  // 만약 ans가 true가 되면 더 이상 탐색하지 않음
            }
        }
    }
}

int main() {
    cin >> m >> n;

    for(int i = 0; i < m; i++)
        for(int j = 0; j < n; j++)
            scanf("%1d", &map[i][j]);

    /*
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            printf("%d ", map[i][j]);
        }
        printf("\n");
    }
    */


    for (int i = 0; i < m; i++) {
        if (map[0][i] == 0) {
            memset(visit, 0, sizeof(visit));
            dfs(0, i);

            if(ans){
                break;
            }
        }
    }

    if (ans) {
        cout << "YES";
    }
    else {
        cout << "NO";
    }

    return 0;
}