
import sys
from collections import deque

input = sys.stdin.readline


# cur 정점의 이웃 정점을 전부 탐색했는지 확인
def check_visit(cur: int, neighbor: list, visited: list):
    for i in neighbor:
        if visited[i] == False:
            return False
    
    return True
        

def solve(N: int, graph: list, visit_seq: list) -> int:
    stack = deque()
    visited = [False for _ in range(N+1)]

    # visit_seq[i]가 올바른 탐색인지 확인
    for i in range(N-1):
        
        cur = visit_seq[i]
        visited[cur] = True

        # 현재 탐색 정점의 자식 정점이 전부 다 방문한 경우
        if check_visit(cur, graph[cur], visited):
            if stack:
                stack.pop()

        # 현재 탐색 정점에 자식 정점이 있고 다음 순서가 자식 정점이라면
        elif len(graph[cur]) != 0:
            stack.append(cur)
            if visit_seq[i+1] in graph[stack[-1]]:
                continue
            # 다음 탐색에 자식 정점을 탐색하지 않는다면
            else:
                return 0
        
        else:
            return 0
    
    return 1


def main():
    N = int(input())

    # 0번 정점은 미사용
    graph = [[] for i in range(N+1)]

    for _ in range(N-1):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    
    visit_seq = list(map(int, input().split()))

    if visit_seq[0] != 1:
        print(0)
        exit()
    print(solve(N, graph, visit_seq))


main()