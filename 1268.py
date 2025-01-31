from collections import defaultdict

n = int(input())
student_classes = []

classes_per_year = [defaultdict(set) for _ in range(5)]
for student_num in range(1, n + 1):
    classes = list(map(int, input().split()))
    student_classes.append(classes)
    for year in range(5):
        class_num = classes[year]
        classes_per_year[year][class_num].add(student_num)

max_shared = -1
ans = 0

for i in range(1, n + 1):
    shared_students = set()
    classes = student_classes[i - 1]
    for year in range(5):
        class_num = classes[year]
        shared_students.update(classes_per_year[year][class_num])
    shared_students.discard(i)
    count = len(shared_students)
    if count > max_shared:
        max_shared = count
        ans = i
    elif count == max_shared and i < ans:
        ans = i

print(ans)
