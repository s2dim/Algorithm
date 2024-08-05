import java.util.Arrays;
import java.util.Scanner;
class Solution
{
	public static void main(String args[]) throws Exception
	{

		Scanner sc = new Scanner(System.in);

		// 테스트케이스 개수 T
		int T = sc.nextInt();

		for (int t = 1; t <= T; t++) {

			// K번 입력 받음
			int K = sc.nextInt();

			int[] arr = new int[K];
			int idx = 0;
			int sum = 0;

			for (int k = 0; k < K; k++) {

				int n = sc.nextInt();

				if (n == 0) {
					sum -= arr[idx-1];
					arr[idx - 1] = 0;
					idx--;
				} else {
					arr[idx] = n;
					sum += n;
					idx++;
					
				}


			}
			System.out.println("#" + t + " " + sum);
		}

	}
}
