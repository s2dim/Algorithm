import java.util.*;
 
class Solution
{
    public static void main(String args[]) throws Exception
    {
 
        Scanner sc = new Scanner(System.in);
 
        int T = sc.nextInt();
 
        for (int t = 1; t <= T; t++) {
 
            int N = sc.nextInt();
 
            // 농장 배열
            int[][] arr = new int[N][N];
 
            for (int i = 0; i < N; i++) {
                String value = sc.next();
                char[] c = value.toCharArray();
 
                for (int j = 0; j < N; j++) {
                    arr[i][j] = Character.getNumericValue(c[j]);
                }
            }
 
            // 0열 ~ 센터열
            int sum = 0;
 
            for (int i = 0; i < (N / 2) + 1; i++) {
                for (int j = (N / 2) - i; j <= (N / 2) + i; j++) {
                    sum += arr[i][j];
 
                }
            }
 
             
            // 이후 ~ N열
            if (N >= 3) {
                int n = 0;
                for (int i = 1; i <= N / 2; i++) {
                    for (int j = 1 + n; j <  N - i; j++) {
                        sum += arr[(N / 2) + i][j];
                    }
                    n++;
                }
            }
            System.out.println("#" + t + " " + sum);
        }
         
    }
 
}