class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        # north, east, south, and west
        # 빌딩의 높이를 맘대로 바꿀 수 있지만, 높이는 각각 달라야한다.
        # skyline (외곽선에 변화없이 최대한 빌딩을 높이기)

        col_grid = list(zip(*grid))
        length = len(grid)
        new_arr = [[0 for _ in range(length)] for _ in range(length)]
        answer = 0
        for i in range(length):
            for j in range(length):
                new_arr[i][j] = max(0, min(max(grid[i]), max(col_grid[j])))
                answer += new_arr[i][j] - grid[i][j]
        return answer
