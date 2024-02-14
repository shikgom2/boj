import sys
input = sys.stdin.readline

def find_min_greater(cards, target, used):
    left, right = 0, len(cards) - 1
    result = -1
    while left <= right:
        mid = (left + right) // 2
        if cards[mid] > target and not used[mid]:
            result = mid
            right = mid - 1
        else:
            left = mid + 1
    while result != -1 and used[result]:
        result += 1
        if result >= len(cards):
            return -1
    return result

def play_game(N, M, K, chosen_cards, chu_cards):
    chosen_cards.sort()
    answer = []
    used = [False] * M

    for chu_card in chu_cards:
        idx = find_min_greater(chosen_cards, chu_card, used)
        if idx != -1:
            answer.append(chosen_cards[idx])
            used[idx] = True
    return answer

N, M, K = map(int, input().split())
chosen_cards = list(map(int, input().split()))
chu_cards = list(map(int, input().split()))

minsu_cards = play_game(N, M, K, chosen_cards, chu_cards)

for card in minsu_cards:
    print(card)