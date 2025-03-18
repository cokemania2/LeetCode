class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        """
        노트에 무작정 적으면서 규칙 찾다보니
        각 위치에서 넣을 수 있는 최댓값을 넣으니 잘 나옴
        """

        row_length = len(rowSum)
        col_length = len(colSum)

        arr = [[0 for _ in range(col_length)] for _ in range(row_length)]

        for i in range(row_length):
            for j in range(col_length):
                x = min(rowSum[i], colSum[j])
                arr[i][j] = x
                rowSum[i] -= x
                colSum[j] -= x

        return arr