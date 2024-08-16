import java.util.*;

public class Solution {

	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);

		int T = sc.nextInt();

		for (int t = 1; t <= T; t++) {

			String str = sc.next();
			char[] arr = str.toCharArray();

			int cnt = 0;
			boolean ball = false;
			boolean weed = false;

			for (int i = 0; i < arr.length; i++) {
				if (arr[i] == '(') {
					ball = true;

				} else if (ball == true && arr[i] == '|') {
					cnt++;
					ball = false;

				} else if (ball == false && arr[i] == '|') {
					ball = false;
					weed = true;

				} else if (ball == true && (arr[i] == ')')) {
					cnt++;
					ball = false;

				} else if (ball == false && weed == true && arr[i] == ')') {
					cnt++;
					weed = false;

				} else if (arr[i] == '.') {
					ball = false;
					weed = false;

				} else if (ball = true && arr[i] == ')') {
					cnt++;
					ball = false;

				}


			}
			System.out.println("#" + t + " " + cnt);

		}
	}
}
