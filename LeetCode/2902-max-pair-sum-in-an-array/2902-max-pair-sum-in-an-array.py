def int_to_int_list(num: int) -> List[int]:
        return list(map(int,list(str(num))))

class Solution:
    def maxSum(self, nums: List[int]) -> int:
        answer = []
        max_digit_dict = dict()
        for num in nums:
            max_digit = max(int_to_int_list(num))
            if max_digit in max_digit_dict:
                max_digit_dict[max_digit].append(num)
            else:
                max_digit_dict[max_digit] = [num]
        for _, num_list in max_digit_dict.items():
            if len(num_list) >= 2:
                answer.append(sum(sorted(num_list, reverse=True)[:2]))
        if len(answer) == 0:
            return -1
        return max(answer)
        