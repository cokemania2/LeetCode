// you can also use imports, for example:
import java.util.*;

// you can write to stdout for debugging purposes, e.g.
// System.out.println("this is a debug message");

class Solution {
    public int solution(String S) {
        // Implement your solution here
        List<String> stack = new ArrayList<>();

        for (int i=0;i<S.length(); i++) {
            if (S.charAt(i) == '(') {
                stack.add("(");
            } else {
                if (stack.size() > 0 && stack.get(stack.size()-1) == "(") {
                    stack.remove(stack.size()-1); 
                } else {
                    stack.add(")");
                }
            }
        }
        if (stack.size() == 0) {
            return 1;
        }
        return 0;
    }
}