import java.util.*;

public class Main {

	static int start, end;

	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);

		int n = sc.nextInt();
		int [] arr = new int[n];

		for (int i = 0; i < n; i++) {
			arr[i] = sc.nextInt();
		}

		// 이진탐색은 기준 배열을 정리해야 함.
		Arrays.sort(arr);

		int m = sc.nextInt();

		for (int i = 0; i < m; i++) {
			int num = sc.nextInt();

			start = 0;
			end = n - 1;


			int ans = bs(arr, num);
			
			System.out.println(ans);
		}

	}

	static int bs(int[] arr, int key) {

		while (start <= end) {
			int mid = (start + end) / 2;

			if (key < arr[mid]) {
				end = mid - 1;
			} else if (key > arr[mid]) {
				start = mid + 1;
			} else {
				return 1;
			}
		}

			return 0;
	}

}
