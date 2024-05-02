class Solution:
    def getGoodIndices(self, variables: List[List[int]], target: int) -> List[int]:
        result = []
        for i, variable in enumerate(variables):
            if self._is_good(variable, target):
                result.append(i)
        return result

    def _is_good(self, variables: list[int], target: int) -> bool:
        a, b, c, m = variables
        return ((a ** b % 10) ** c) % m == target
