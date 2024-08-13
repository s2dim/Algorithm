import java.util.*;
 
public class Solution {
 
    public static void main(String[] args) {
 
        Scanner sc = new Scanner(System.in);
        StringBuilder sb = new StringBuilder();
 
        for (int t = 1; t <= 10; t++) {
            int N = sc.nextInt();
 
            LinkedList<Integer> lst = new LinkedList<>();
 
            for (int i = 0; i < N; i++) {
                lst.add(sc.nextInt());
            }
            int purple = sc.nextInt();
 
            for (int j = 0; j < purple; j++) {
                String s = sc.next();
                if (s.equals("I")) {
                    int idx = sc.nextInt();
                    int n = sc.nextInt();
                    for (int k = 0; k < n; k++) {
                        lst.add(idx + k, sc.nextInt());
                    }
                } else if (s.equals("D")) {
                    int x = sc.nextInt();
                    int y = sc.nextInt();
 
                    for (int k = 0; k < y; k++) {
                        lst.remove(x);
                    }
                } else if (s.equals("A")) {
                    int n = sc.nextInt();
                    for (int k = 0; k < n; k++) {
                        lst.addLast(sc.nextInt());
                    }
 
                }
            }
 
            for (int i = 0; i < 10; i++) {
                sb.append(lst.get(i) + " ");
            }
 
            System.out.println("#" + t + " " + sb);
            sb.setLength(0);
 
        }
 
    }
 
}