import java.util.*;
 
public class Solution {
    public static void main(String[] args) {
 
        Scanner sc = new Scanner(System.in);
 
        int T = sc.nextInt();
        StringBuilder sb = new StringBuilder();
 
        for (int t = 1; t <= T; t++) {
 
            int N = sc.nextInt();
            PriorityQueue<Integer> pq = new PriorityQueue<>(Collections.reverseOrder());
 
            for (int i = 0; i < N; i++) {
                int n = sc.nextInt();
 
                if (n == 1) {
                    int plus = sc.nextInt();
                    pq.add(plus);
                } else if (n == 2) {
                    if (!(pq.isEmpty())) {
                        int a = pq.poll();
                        sb.append(a);
                    } else {
                        sb.append(-1);
                    }
                    sb.append(" ");
                }
            }
            System.out.println("#" + t + " " + sb);
 
            sb.setLength(0);
        }
 
    }
 
}