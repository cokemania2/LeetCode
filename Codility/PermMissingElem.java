// 1.	등차수열 합 공식 사용
// 2.	배열의 실제 합 계산
// 3.	차이 계산

import java.util.*;

class Solution {
    public int solution(int[] A) {
        int N = A.length;
        long totalSum = (long) (N + 1) * (N + 2) / 2;
        
        long actualSum = 0;
        for (int num : A) {
            actualSum += num;
        }
        
        return (int) (totalSum - actualSum);
    }
}