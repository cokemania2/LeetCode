// you can also use imports, for example:
// import java.util.*;

// you can write to stdout for debugging purposes, e.g.
// System.out.println("this is a debug message");

class Solution {
    public int solution(int X, int[] A) {
        boolean[] array = new boolean[X];
        int count = 0;

        // 모든 값이 false로 초기화됨
        for (int i = 0; i < array.length; i++) {
            array[i] = false;
        }

        for (int i=0; i<A.length; i++) {
            if (array[A[i] - 1] == false) {
                array[A[i] - 1] = true;
                count += 1;
            }
            if (count == X) {
                return i;
            }
        }

        return -1;
    }
}