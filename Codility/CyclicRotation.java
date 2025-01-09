class Solution {
    public int[] solution(int[] A, int K) {
        if (A.length == 0) { // 빈 배열 처리
            return A;
        }

        int[] newArr = new int[A.length];
        K %= A.length; // K를 배열 길이로 나눈 나머지로 업데이트

        for (int i = 0; i < A.length; i++) {
            newArr[(i + K) % A.length] = A[i];
        }

        return newArr;
    }
}
