import java.util.*;

class Solution {
    public int solution(String s) {
        int answer = 0;

        char x = s.charAt(0);
        int x_i = 1;
        int y_i = 0;

        for (int i=1; i<s.length(); i++) {
            if (x_i == 0 || x == s.charAt(i)) {
                x = s.charAt(i);
                x_i += 1;
            } else {
                y_i += 1;
            }
            if (x_i == y_i) {
                x_i = 0;
                y_i = 0;
                answer += 1;
            }
        }

        if (x_i == y_i) {
            return answer;
        }
        return answer + 1;
        
    }
}