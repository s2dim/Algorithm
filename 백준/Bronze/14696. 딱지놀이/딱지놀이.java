import java.util.Scanner;

public class Main {

	public static void main(String[] args) {

		// 별 4 동그라미 3 네모 2 세모 1

		Scanner sc = new Scanner(System.in);

		int N = sc.nextInt();

		for (int i = 0; i < N; i++) {
			int[] a_card = new int[5];
			int[] b_card = new int[5];

			int a = sc.nextInt();
			for (int j = 0; j < a; j++) {
				int score = sc.nextInt();
				a_card[score]++;
			}

			int b = sc.nextInt();
			for (int j = 0; j < b; j++) {
				int score = sc.nextInt();
				b_card[score]++;

			}

			int a_sum = a_card[1] * 1 + a_card[2] * 1000 + a_card[3] * 1000000 + a_card[4] * 1000000000;
			int b_sum = b_card[1] * 1 + b_card[2] * 1000 + b_card[3] * 1000000 + b_card[4] * 1000000000;

			if (a_card[4] > b_card[4]) {
				System.out.println("A");
			} else if (a_card[4] < b_card[4]) {
				System.out.println("B");
			} else {
				if (a_card[3] > b_card[3]) {
					System.out.println("A");
				} else if (a_card[3] < b_card[3]) {
					System.out.println("B");
				} else {
					if (a_card[2] > b_card[2]) {
						System.out.println("A");
					} else if (a_card[2] < b_card[2]) {
						System.out.println("B");
					} else {
						if (a_card[1] > b_card[1]) {
							System.out.println("A");
						} else if (a_card[1] < b_card[1]) {
							System.out.println("B");
						} else {
							System.out.println("D");
						}
					}

				}
			}
		}

	}
}
