li = {
    0: ["0000", "0  0", "0  0", "0  0", "0000"],
    1: ["   1", "   1", "   1", "   1", "   1"],
    2: ["2222", "   2", "2222", "2", "2222"],
    3: ["3333", "   3", "3333", "   3", "3333"],
    4: ["4  4", "4  4", "4444", "   4", "   4"],
    5: ["5555", "5", "5555", "   5", "5555"],
    6: ["6666", "6", "6666", "6  6", "6666"],
    7: ["7777", "   7", "   7", "   7", "   7"],
    8: ["8888", "8  8", "8888", "8  8", "8888"],
    9: ["9999", "9  9", "9999", "   9", "   9"],
}
n = input()
for i in n[:-1]:
    for line in li[int(i)]:
        print(line)
    print()

for line in li[int(n[-1])]:
    print(line)