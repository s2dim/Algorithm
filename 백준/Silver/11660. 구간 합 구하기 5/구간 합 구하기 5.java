

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int M = sc.nextInt();

        int[][] arr = new int[N+1][N+1]; // 배열
        int[][] sum = new int[N+1][N+1]; // 합 배열

        // 배열 입력 받기
        for (int i = 1; i < N+1; i++) {
            for (int j = 1; j < N+1; j++) {
                arr[i][j] = sc.nextInt();
            }
        }

        // 합 배열 작성
        for (int i = 1; i < N+1; i++) {
            for (int j = 1; j < N+1; j++) {
                sum[i][j] = arr[i][j] + sum[i][j-1] + sum[i-1][j]  - sum[i-1][j-1];
            }
        }

        for (int i = 0; i < M; i++) {
            int x1 = sc.nextInt();
            int y1 = sc.nextInt();
            int x2 = sc.nextInt();
            int y2 = sc.nextInt();

            int ans = sum[x2][y2] - sum[x1-1][y2] - sum[x2][y1-1] + sum[x1-1][y1-1];
            System.out.println(ans);
        }
    }
}