#include <stdio.h>
#include <stdlib.h>

int N;
int board[15][15]; 
long long int count = 0;

int isSafe(int row, int col) {
    int i, j;
    
    // 같은 열
    for (i = 0; i < row; i++)
        if (board[i][col])
            return 0;
    
    // 왼쪽 대각선
    for (i = row, j = col; i >= 0 && j >= 0; i--, j--)
        if (board[i][j])
            return 0;
    
    // 오른쪽 대각선
    for (i = row, j = col; i >= 0 && j < N; i--, j++)
        if (board[i][j])
            return 0;
    
    return 1;
}
int solveNQUtil(int row) {
    if (row >= N) {
        count++;
        return 0; 
    }
    
    for (int col = 0; col < N; col++) {
        if (isSafe(row, col)) {
            board[row][col] = 1;
            solveNQUtil(row + 1);
            board[row][col] = 0;
        }
    }
    
    return 0;
}

void solveNQ() {
    solveNQUtil(0);
    printf("%lld", count);
}

int main() {
    scanf("%d", &N);
    
    for (int i = 0; i < N; i++)
        for (int j = 0; j < N; j++)
            board[i][j] = 0;
    
    solveNQ();
    return 0;
}