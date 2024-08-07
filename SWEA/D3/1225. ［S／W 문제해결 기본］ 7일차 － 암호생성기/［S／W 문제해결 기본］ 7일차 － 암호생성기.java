import java.util.*;
 
class Solution
{
    public static void main(String args[]) throws Exception
    {
        Scanner sc = new Scanner(System.in);
 
 
        for (int t = 1; t <= 10; t++) {
            sc.nextInt();
            Queue<Integer> queue = new LinkedList<>();
 
            for (int i = 1; i <= 8; i++) {
                int num = sc.nextInt();
                queue.add(num);
            }
 
            // 초기값 지정
            int new_n = 1;
            int n = 1;
 
            while (true) {
                if (n > 5)
                    n = 1;
 
                new_n = queue.poll();
                new_n -= n;
                 
                if (new_n <= 0) {
                    new_n = 0;
                    queue.add(new_n);
                    break;
                }
                queue.add(new_n);
                n++;
            }
             
            String res = "";
            for (int i = 0; i < 8; i++) {
                 
                int num = queue.poll();
                res += num;
                res += " ";
            }
            System.out.println("#" + t + " " + res);
        }
 
    }
}