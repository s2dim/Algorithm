import java.util.*;
 
public class Solution {
 
    public static void main(String[] args) {
 
        Scanner sc = new Scanner(System.in);
 
        int T = sc.nextInt();
 
        for (int t = 1; t <= T; t++) {
            // N개의 정수
            int N = sc.nextInt();
            int[] arr = new int[N];
 
            // 배열에 숫자 담기
            for (int i = 0; i < N; i++) {
                arr[i] = sc.nextInt();
            }
 
            int res = -1;
 
            // 곱 리스트에 담기
            for (int i = 0; i < N; i++) {
                for (int j = i + 1; j < N; j++) {
                    int product = arr[i] * arr[j];
                    if (check(product)) {
                        res = Math.max(res, product);
                    }
 
                }
 
            }
            System.out.println("#" + t + " " + res);
 
        }
 
    }
 
    static boolean check(int num) {
        int max = 10;
 
        while (num > 0) {
            int digit = num % 10;
            if (digit > max) {
                return false;
            }
            max = digit;
            num /= 10;
 
        }
        return true;
    }
 
}