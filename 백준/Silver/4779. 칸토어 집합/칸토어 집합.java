
import java.util.Scanner;

public class Main {

	static StringBuilder sb;

	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);

		while (sc.hasNext()) {
			String num = sc.next();
			int N = Integer.parseInt(num);

			sb = new StringBuilder();

			for (int i = 0; i < Math.pow(3, N); i++) {
				sb.append("-");
			}

			int len = (int) Math.pow(3, N);

			cal(0, len);
			System.out.println(sb);
			sb.setLength(0);
		}
	}

	static void cal(int start, int len) {
		if (len == 1) {
			return;
		}

		int change = len / 3;
		int end = start + change * 2;

		for (int i = start + change; i < end; i++) {
			sb.setCharAt(i, ' ');
		}

		cal(start, change);
		cal(end, change);
	}

}
