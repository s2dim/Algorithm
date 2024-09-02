import java.util.Arrays;
import java.util.Scanner;

public class Main {

	static int a;
	static int k;
	static int[] arr;
	static int[] sortArr;
	static int cnt = 0;
	static int ans = -1;
	

	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);

		a = sc.nextInt();
		k = sc.nextInt();

		arr = new int[a];
		sortArr = new int[a];

		for (int i = 0; i < a; i++) {
			arr[i] = sc.nextInt();
		}
		
		mergeSort(0, a-1);
		System.out.println(ans);

	}

	static void mergeSort(int left, int right) {

		if (left < right) {
			int mid = (left + right) / 2;
			mergeSort(left, mid);
			mergeSort(mid + 1, right);
			merge(left, mid, right);
		}
	}

	static void merge(int left, int mid, int right) {
		int L = left;
		int R = mid + 1;
		int idx = left;

		while (L <= mid && R <= right) {
			if (arr[L] <= arr[R])
				sortArr[idx++] = arr[L++];
			else
				sortArr[idx++] = arr[R++];
		}
		if (L <= mid) {
			for (int i = L; i <= mid; i++) {
				sortArr[idx++] = arr[i];
			}
		} else {
			for (int i = R; i <= right; i++) {
				sortArr[idx++] = arr[i];
			}
		}

		for (int i = left; i <= right; i++) {
			arr[i] = sortArr[i];
			cnt++;
			
			if (cnt == k) {
				ans = arr[i];
			}
	
		}
	}

}
