import java.util.Scanner;

public class Solution {

	static int a;
	static int b;
	static int ans = 1;

	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);

		for (int t = 1; t <= 10; t++) {
			sc.nextInt();

			a = sc.nextInt();
			b = sc.nextInt();
			
			System.out.print("#" + t + " ");
			power(b);
			ans = 1;

		}
	}

	static void power(int cnt) {

		if (cnt == 0 ) {
			System.out.println(ans);
			return;
		}

		else {
			ans *= a;
			power(cnt - 1);

		}
	}

}
