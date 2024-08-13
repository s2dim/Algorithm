import java.util.Scanner;

public class Main {
	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);

		int T = sc.nextInt();

		for (int t = 0; t < T; t++) {
			String str = sc.next();

			char[] c = str.toCharArray();

			int score = 0;
			int idx = 0;

			int[] scoreArr = new int [80];
			
			for (int i = 0; i < 80; i++) {
				scoreArr[i] = i + 1;
			}
			

			for (char d : c) {
				if (d == 'O') {
					score += scoreArr[idx];
					idx++;
				} else {
					idx = 0;
				}
			}
			System.out.println(score);
		}

	}

}
