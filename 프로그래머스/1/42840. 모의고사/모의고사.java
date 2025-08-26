import java.util.*;

class Solution {
    public int[] solution(int[] answers) {
        
        int a = 0;
        int b = 0;
        int c = 0;
        
        int[] one = {1, 2, 3, 4, 5}; // 5  = (n % 5) - 1
        int[] second = {2, 1, 2, 3, 2, 4, 2, 5}; // 8 = (n % 8) - 1
        int[] third = {3, 3, 1, 1, 2, 2, 4, 4, 5, 5}; // 10 = (n % 10) - 1
        
        
        System.out.println(Arrays.toString(answers));
        
        for (int i = 0; i < answers.length; i++) {
            if (answers[i] == one[i % 5]) {
                a += 1;
            }
            if (answers[i] == second[i % 8]) {
                b += 1;
            }
            if (answers[i] == third[i % 10]) {
                c += 1;
            }
        }
        
        ArrayList<Integer> result = new ArrayList<>();
        int max = Math.max(Math.max(a, b), c);
        if (max == a) 
            result.add(1);
        if (max == b)
            result.add(2);
        if (max == c)
            result.add(3);
        
        Collections.sort(result);
        
        int[] answer2 = new int[result.size()];
        int idx = 0;
        for (int x : result){
            answer2[idx++] = x;
        }
        return answer2;
    }
}
