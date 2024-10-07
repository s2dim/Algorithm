import java.util.*;

public class Main {

	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);

		int n = sc.nextInt();
		int[] arr = new int[n];

		for (int i = 0; i < n; i++) {
			arr[i] = sc.nextInt();
		}

		Arrays.sort(arr);

		int m = sc.nextInt();

		StringBuilder sb = new StringBuilder();

		for (int i = 0; i < m; i++) {
			int num = sc.nextInt();
			int lowerbound = lowerbound(arr, num);
			int upperbound = upperbound(arr, num);
			
			int cnt = upperbound - lowerbound;
			sb.append(cnt + " ");

		}
		System.out.println(sb);
		sc.close();

	}

	static int lowerbound(int[] arr, int key) {

		int lo = 0;
		int hi = arr.length;

		while (lo < hi) {
			int mid = (lo + hi) / 2;

			if (key <= arr[mid]) {
				hi = mid;
			} else if (key > arr[mid]) {
				lo = mid + 1;
			}
		}

		return lo;

	}

	static int upperbound(int[] arr, int key) {

		int lo = 0;
		int hi = arr.length;

		while (lo < hi) {
			int mid = (lo + hi) / 2;

			if (key < arr[mid]) {
				hi = mid;
			} else if (key >= arr[mid]) {
				lo = mid + 1;
			}
		}

		return lo;

	}

}
