import java.util.*;

public class Solution {

	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);

		// T 입력 받기
		int T = sc.nextInt();

		for (int t = 1; t <= T; t++) {
			int n = sc.nextInt();
			int m = sc.nextInt();

			char[][] arr = new char[n][m];

			int[][] colorCount = new int[n][3];

			// 배열 만들기
			for (int i = 0; i < n; i++) {
				String c = sc.next();
				arr[i] = c.toCharArray();
				colorCount[i] = cntFlag(arr, i, n, m);
			}

			// cnt 초기화
			int cnt = 100000;
			
			// start 파란색 시작 인덱스, end 파란색 끝 인덱스
			for (int start = 1; start < n - 1; start++) {
				for (int end = start + 1; end < n; end++) {
					int cntt = 0;

					// 흰색 자리
					for (int i = 0; i < start; i++) {
						cntt += colorCount[i][1] + colorCount[i][2];
					}

					// 파랑 자리
					for (int i = start; i < end; i++) {
						cntt += colorCount[i][0] + colorCount[i][2];
					}

					// 빨강 자리
					for (int i = end; i < n; i++) {
						cntt += colorCount[i][0] + colorCount[i][1];
					}
					cnt = Math.min(cnt,  cntt);
				}
			}
			System.out.println("#" + t + " " + cnt);
		}

	}

	// 개수 세는 배열 생성
	static int[] cntFlag(char[][] arr, int r, int n, int m) {
		// [0] : W [1] : B [2] : R
		int[] flag = new int[3];

		for (int i = 0; i < m; i++) {
			if (arr[r][i] == 'W') {
				flag[0]++;
			} else if (arr[r][i] == 'B') {
				flag[1]++;
			} else {
				flag[2]++;
			}
		}

		return flag;

	}

}