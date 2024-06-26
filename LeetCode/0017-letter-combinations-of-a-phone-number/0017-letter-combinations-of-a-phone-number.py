import itertools

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []

        digit_alphabet_dict: dict[str: list[str]] = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u" ,"v"],
            "9": ["w", "x", "y", "z"]
        }
        digit_list = list(digits)
        combinations = itertools.product(*[digit_alphabet_dict[digit] for digit in digit_list])
        result = ["".join(combination) for combination in list(combinations)]
        return result