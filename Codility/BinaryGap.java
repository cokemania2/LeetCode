class Solution {
    public int solution(int N) {
        String binary = Integer.toBinaryString(N);
        int binaryGaps = 0;
        int maxBinaryGaps = 0;

        for (int i=0; i < binary.length(); i++) {
            if (binary.charAt(i) == '1') {
                maxBinaryGaps = Math.max(binaryGaps, maxBinaryGaps);
                binaryGaps = 0;
            } else {
                binaryGaps += 1;
            }
        }
        return maxBinaryGaps;
    }
}
