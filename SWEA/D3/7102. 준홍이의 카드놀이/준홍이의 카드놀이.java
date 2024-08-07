import java.util.*;
 
class Solution
{
    public static void main(String args[]) throws Exception
    {
            Scanner sc = new Scanner(System.in);
        int T = sc.nextInt();
 
        for (int t = 1; t <= T; t++) {
            int n = sc.nextInt();
            int m = sc.nextInt();
 
            int[] arr = new int[(n * m) + 1];
            int[] arr2 = new int[(n * m) + 1];
            String res = "";
 
            for (int i = 1; i <= n; i++) {
                for (int j = 1; j <= m; j++) {
 
                    int sum = i + j;
                    arr[sum]++;
                    arr2[sum]++;
                }
            }
 
            Arrays.sort(arr2);
            int max = arr2[(n * m)];
 
             
            for (int i = 1; i <= (n*m); i++) {
                if (arr[i] == max) {
                    res += i;
                    res += " ";
                }
            }
            System.out.println("#" + t + " " + res);
        }
    }
}