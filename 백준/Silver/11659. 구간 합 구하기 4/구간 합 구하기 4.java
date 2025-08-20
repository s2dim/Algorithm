import java.util.*;

public class Main {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        int m = sc.nextInt();
        int[] arr = new int[n+1];
        int[] sum = new int[n+1];

        for (int i = 1; i < n+1; i++) {
            arr[i] = sc.nextInt();
            sum[i] += sum[i-1] + arr[i];
        }
        
        for (int i = 0; i < m; i++) {
            int start = sc.nextInt();
            int end = sc.nextInt();

            System.out.println(sum[end]-sum[start-1]);
        }

    }
}
