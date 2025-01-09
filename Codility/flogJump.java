class Solution {
    public int solution(int X, int Y, int D) {
        // Implement your solution here
        float answer = (float)(Y - X) / D;
        int rounedAnswer = Math. (answer);
        
        if (rounedAnswer == answer) {
            return rounedAnswer;
        }
        return  rounedAnswer + 1;
    }
}
