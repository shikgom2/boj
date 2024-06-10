import sys
input = sys.stdin.readline

def dfs(t):
	flag = True
	i = 2
	while i * i <= t: 
		if(t % i == 0):
			flag = False
			break
		i += 1

	if flag:
		for i in range(1,10):
			dfs(t*10 + i)
	else: 
		return 
	
	if len(str(t)) == m:
		print(t)
		return
		
m = int(input())
for i in range(2,10):
	go(i)