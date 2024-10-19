def main():
    import sys
    input = sys.stdin.readline

    n = int(input())
    directions = input().strip()
    heights = list(map(int, input().split()))

    removed = [False] * n

    # Process eels facing left
    max_height_left = 0
    for i in range(n):
        if directions[i] == 'L':
            if max_height_left >= heights[i]:
                removed[i] = True  # Mark eel for removal
        max_height_left = max(max_height_left, heights[i])  # Update max height regardless of direction

    # Process eels facing right
    max_height_right = 0
    for i in range(n - 1, -1, -1):
        if directions[i] == 'R':
            if max_height_right >= heights[i]:
                removed[i] = True  # Mark eel for removal
        max_height_right = max(max_height_right, heights[i])  # Update max height regardless of direction

    # Count the number of eels to remove
    eels_to_remove = sum(removed)
    print(eels_to_remove)

if __name__ == "__main__":
    main()
def main():
    import sys
    input = sys.stdin.readline

    n = int(input())
    directions = input().strip()
    heights = list(map(int, input().split()))

    removed = [False] * n

    # Process eels facing left
    max_height_left = 0
    for i in range(n):
        if directions[i] == 'L':
            if max_height_left >= heights[i]:
                removed[i] = True  # Mark eel for removal
        max_height_left = max(max_height_left, heights[i])  # Update max height regardless of direction

    # Process eels facing right
    max_height_right = 0
    for i in range(n - 1, -1, -1):
        if directions[i] == 'R':
            if max_height_right >= heights[i]:
                removed[i] = True  # Mark eel for removal
        max_height_right = max(max_height_right, heights[i])  # Update max height regardless of direction

    # Count the number of eels to remove
    eels_to_remove = sum(removed)
    print(eels_to_remove)

if __name__ == "__main__":
    main()
