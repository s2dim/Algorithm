import java.util.Scanner;

class Solution
{
	public static void main(String args[]) throws Exception
	{
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		for (int i = 1; i <= n; i++) {
			int sum = 0;
			for (int j = 0; j < 10; j++) {
				int a = sc.nextInt();

				if (a % 2 != 0) {
					sum += a;
				}
			}
			System.out.println("#" + i + " " + sum);
		}
	}
}