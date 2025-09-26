import java.util.*;

public class Solution {
    public int[] solution(int []arr) {
        ArrayList<Integer> arrAnswer = new ArrayList<>();
        int before = -1;
        
        for (int i = 0; i < arr.length; i++) {
            int n = arr[i];
            if (before != n) {
                arrAnswer.add(n);
                before = n;
            }
        }
        int[] answer = arrAnswer.stream().mapToInt(Integer::intValue).toArray();
        return answer;
    }
}