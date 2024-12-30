class Solution:
    def romanToInt(self, s: str) -> int:
        roman_to_value = {
            'I': 1, 'V': 5, 'X': 10,
            'L': 50, 'C': 100, 'D': 500, 'M': 1000
        }
        
        answer = 0
        prev_value = 0
        
        for char in s:
            curr_value = roman_to_value[char]
            if curr_value > prev_value:
                # Special case: subtract twice the previous value (undo previous addition)
                answer += curr_value - 2 * prev_value
            else:
                answer += curr_value
            prev_value = curr_value
        
        return answer