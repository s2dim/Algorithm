import java.util.*;

public class Main {

	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);

		int[] arr = new int[10];

		// 배열 생성
		for (int i = 0; i < 10; i++) {
			arr[i] = sc.nextInt();
		}

		int sum = 0;
		int sum2 = 0;
		int ans = 0;

		for (int i = 0; i < 10; i++) {
			sum += arr[i];
			if (sum >= 100) {
				sum2 = sum - arr[i];
				if ((sum - 100) == (100 - sum2))
					ans = sum;
				else {
					if (sum - 100 > 100 - sum2) {
						ans = sum2;
					} else
						ans = sum;
				}
				break;
			} else
				ans = sum;
		}
		System.out.println(ans);

	}

}
