import java.util.*;

public class Main {
	// 2024-08-16

	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);

		int button = sc.nextInt();

		int[] arr = new int[button + 1];

		for (int i = 1; i <= button; i++) {
			arr[i] = sc.nextInt();
		}

		int n = sc.nextInt();

		for (int i = 0; i < n; i++) {
			int gender = sc.nextInt();
			int num = sc.nextInt();

			if (gender == 1) {
				int cnt = 1;

				while (num * cnt <= button) {
					turn(arr, num * cnt);
					cnt++;
				}

			} else {
				if (num <= 1 || num == button) {
					turn(arr, num);
				} else if (arr[num - 1] != arr[num + 1]) {
					turn(arr, num);
				} else {
					int cnt = 2;
					while (num - cnt >= 1 && num + cnt <= button && arr[num - cnt] == arr[num + cnt]) {
						cnt++;
					}

					cnt = cnt - 1;
					for (int j = num - cnt; j <= num + cnt; j++) {
						turn(arr, j);
					}
				}
			}
		}

		StringBuilder sb = new StringBuilder();

		int line = 20;

        for (int i = 1; i <= button; i++) {
            sb.append(arr[i]).append(" ");
            if (i % line == 0) {
                sb.append("\n");
            }
        }

        System.out.print(sb);
    }
	static int[] turn(int arr[], int num) {
//		if (arr[num] == 1) {
//			arr[num] = 0;
//		} else {
//			arr[num] = 1;
//		}
		arr[num] = 1 - arr[num];

		return arr;
	}

}
