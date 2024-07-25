def minimize_advantage(test_cases):
    results = []
    
    for case in test_cases:
        N, cookies = case
        cookies.sort(reverse=True)
        
        zbyszek_sum = 0
        hektor_sum = 0
        
        # 현재 쿠키 집합으로 우위를 계산
        for i in range(N):
            if i % 2 == 0:
                zbyszek_sum += cookies[i]
            else:
                hektor_sum += cookies[i]
        
        current_difference = zbyszek_sum - hektor_sum
        min_difference = current_difference
        
        # 쿠키를 추가하여 우위 최소화 시도
        for new_cookie in range(1001):
            new_zbyszek_sum = zbyszek_sum
            new_hektor_sum = hektor_sum
            
            if N % 2 == 0:
                new_zbyszek_sum += new_cookie
            else:
                new_hektor_sum += new_cookie
            
            new_difference = new_zbyszek_sum - new_hektor_sum
            min_difference = min(min_difference, new_difference)
        
        results.append(min_difference)
    
    return results

# 입력 받기
Z = int(input().strip())
test_cases = []

for _ in range(Z):
    N = int(input().strip())
    cookies = list(map(int, input().strip().split()))
    test_cases.append((N, cookies))

# 결과 계산
results = minimize_advantage(test_cases)

# 출력
for result in results:
    print(result)
