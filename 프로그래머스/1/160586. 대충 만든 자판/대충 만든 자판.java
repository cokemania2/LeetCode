import java.util.*;

class Solution {
    public int[] solution(String[] keymap, String[] targets) {
        HashMap<Character, Integer> shortCut = new HashMap<>();
        
        for (String key: keymap) {
            for (int i = 0; i < key.length(); i++) {
                char c = key.charAt(i);
                if (shortCut.containsKey(c)) {
                    int time = shortCut.get(c);
                    if (time > i + 1) {
                        shortCut.replace(c, i + 1);
                    }
                } else {
                    shortCut.put(c, i + 1);
                }
            }
        }
        
        List<Integer> answer2 = new ArrayList<>();
            for (String target: targets) {
                int key_sum = 0;
                for (char c: target.toCharArray()) {
                    if (shortCut.containsKey(c)) {
                        key_sum += shortCut.get(c);
                    } else {
                        key_sum = -1;
                        break;
                    }
                }
                answer2.add(key_sum);
            }

        int[] answer = answer2.stream()
                .mapToInt(Integer::intValue)
                .toArray();
        return answer;
    }
}