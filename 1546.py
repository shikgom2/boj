i = int(input())
numbers = [int(x) for x in input().split()]
max_score = max(numbers)
for i in range(0, len(numbers)):
    numbers[i] = numbers[i] / max_score * 100

print(sum(numbers) / len(numbers))