import java.util.Scanner;

public class Main {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();
        int[] score = new int[N];
        float max = 0;

        // 배열에 넣기
        for (int i = 0; i < N; i++) {
            int n = sc.nextInt();
            score[i] = n;
            if (n > max)
                max = n;
        }

        float sum = 0;
        for (int i = 0; i < N; i++) {
            sum += (score[i] / max) * 100;
        }

        float result = sum / N;

        System.out.println(result);
    }
}