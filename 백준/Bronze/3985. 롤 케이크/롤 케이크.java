import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Scanner;

public class Main {

	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);

		int cake = sc.nextInt();

		int n = sc.nextInt();

		int[] cake_arr = new int[cake+1];
		int[] many = new int[n+1];
		int[] cnt = new int[n+1];
		
		for (int i = 1; i <= n; i++) {

			int a = sc.nextInt();
			int b = sc.nextInt();
			
			// 원하는 양 many 배열에 저장
			many[i] = b - a;
			// 아직 남아있는 케이크인지 판단
			for (int j = a; j <= b; j++) {
				if (cake_arr[j] == 0) {
					cake_arr[j] = 1;
					cnt[i] += 1;
				}
			}
		}
		
		// 기대하는 최댓값을 찾기 위해 초기화 진행
		int max = 0;
		int max_idx = -1;

		// 실제 받은 양 최댓값을 찾기 위해 초기화 진행
		int real = 0;
		int real_idx = -1;

		for (int i = 1; i <= n; i++) {
			if (many[i] > max) {
				max = many[i];
				max_idx = i;
			}
			if (cnt[i] > real) {
				real = cnt[i];
				real_idx = i;
			}

		}
		System.out.println(max_idx);
		System.out.println(real_idx);
	}

}
