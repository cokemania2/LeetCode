class Solution {
    public int solution(int n) {
        int answer = 0;
        
        double x = Math.sqrt(n);
        if (Math.round(x) == x) {
            return 1;
        } else{
            return 2;
        }
    }
}