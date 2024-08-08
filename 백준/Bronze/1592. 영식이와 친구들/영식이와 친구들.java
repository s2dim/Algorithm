import java.util.Arrays;
import java.util.Scanner;

public class Main {
	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);

		// n : 인원 수, m : 한 사람이 받을 횟수, l : 공받 횟수 홀수 - 시계방향 l번째, 짝수 - 반시계 l번째
		int n = sc.nextInt();
		int m = sc.nextInt();
		int l = sc.nextInt();

		int[] arr = new int[n];
		int idx = 0;
		int cnt = 0;

		// 첫 사람에게 횟수 + 1
		arr[idx] = 1;

		while (true) {
			if (arr[idx] == m)
				break;
			else if (arr[idx] % 2 == 0) {
				idx = (idx + (n - l)) % n;
				cnt++;
				arr[idx]++;

			} else if (arr[idx] % 2 != 0) {
				idx = (idx + l) % n;
				cnt++;
				arr[idx]++;
			}

		}

		System.out.println(cnt);

	}
}