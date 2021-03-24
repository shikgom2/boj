#include <cstdio>
#include <algorithm>
#include <queue>

using namespace std;

int main() {
	int n, x;
	priority_queue<int> pq;	
    
	scanf("%d", &n);
    for (int i = 0; i < n*n; i++) {
        scanf("%d", &x);
        if (pq.size() < n)
            pq.push(-x);
        else {
            if (-pq.top() < x) {
                pq.pop();
                pq.push(-x);
            }
            else
                continue;
        }
    }
    printf("%d\n", -pq.top());
    return 0;
}
