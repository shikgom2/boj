def find_central_string(A, B, C):
    n = len(A)
    aab_count = 0
    abc_count = 0
    central_string = []

    for i in range(n):
        chars = [A[i], B[i], C[i]]
        chars.sort()
        
        # If all characters are the same
        if chars[0] == chars[2]:
            central_string.append(chars[0])
        
        # If two characters are the same
        elif chars[0] == chars[1] or chars[1] == chars[2]:
            central_string.append(chars[1])
            aab_count += 1
        
        # If all characters are different
        else:
            central_string.append(chars[1])
            abc_count += 1
    
    return ''.join(central_string), abc_count, aab_count

def calculate_distance(P, Q):
    return sum(1 for p, q in zip(P, Q) if p != q)

def main():
    A = input().strip()
    B = input().strip()
    C = input().strip()
    
    central_string, abc_count, aab_count = find_central_string(A, B, C)
    
    # Calculate maximum distance from A, B, C to central_string
    max_distance = max(calculate_distance(central_string, A),
                       calculate_distance(central_string, B),
                       calculate_distance(central_string, C))
    
    print(max_distance)
    print(central_string)

# Example usage
main()
