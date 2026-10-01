from collections import Counter

def count_valid_permutations(s: str) -> int:
    counter = Counter(s)
    total_length = len(s)
    
    def backtrack(length_left: int, last_char: str) -> int:
        if length_left == 0:
            return 1
            
        count = 0
        for char in list(counter.keys()):
            if char == last_char:
                continue
            if counter[char] > 0:
                counter[char] -= 1
                
                count += backtrack(length_left - 1, char)
                
                counter[char] += 1
                
        return count

    return backtrack(total_length, "")

print(count_valid_permutations(input()))