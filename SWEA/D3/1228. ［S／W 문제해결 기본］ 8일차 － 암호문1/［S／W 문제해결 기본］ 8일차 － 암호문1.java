import java.util.*;
 
public class Solution {
 
    public static void main(String[] args) {
 
        Scanner sc = new Scanner(System.in);
        StringBuilder sb = new StringBuilder();
 
        for (int t = 1; t <= 10; t++) {
            int N = sc.nextInt();
 
            LinkedList<Integer> lst = new LinkedList<>();
 
            for (int n = 0; n < N; n++) {
                lst.add(sc.nextInt());
            }
 
 
            int purple = sc.nextInt();
 
            for (int i = 0; i < purple; i++) {
                LinkedList<Integer> lst2 = new LinkedList<>();
                String s = sc.next();
                int idx = sc.nextInt();
                int n = sc.nextInt();
                for (int j = 0; j < n; j++) {
                    lst2.add(sc.nextInt());
                }
                lst.addAll(idx, lst2);
            }
             
             
            for (int i = 0; i < 10; i++) {
                sb.append(lst.get(i) + " ");
            }
             
            System.out.println("#" + t + " " + sb);
            sb.setLength(0);
        }
 
    }
}