import java.util.*;

public class Main {
	public static void main(String[] args) {

		// 동 1 서 2 남 3 북 4
		// ㄱ 모양 (1 3)
		// ㄴ 모양 (2 4)
		// ┏ 모양 (1 4)
		// ┛ 모양 (1 2)

		Scanner sc = new Scanner(System.in);

		int melon = sc.nextInt();

		int[] cnt = new int[5]; // 동서남북 개수 배열
		int[] way = new int[6]; // 동서남북 배열
		int[] len = new int[6]; // 길이 배열

		for (int i = 0; i < 12; i++) {
			int n = sc.nextInt();
			if (i % 2 == 0) {
				cnt[n]++;
				way[i / 2] = n;
			} else {
				len[i / 2] = n;
			}
		}

		// cnt 중 동서남북 개수가 하나만 들어간 방향 담을 리스트
		List<Integer> one = new ArrayList<>();
		// cnt 중 동서남북 개수가 두 개 들어간 방향 담을 리스트
		List<Integer> two = new ArrayList<>();

		//
		for (int i = 1; i < 5; i++) {
			if (cnt[i] == 2)
				two.add(i);
			else
				one.add(i);
		}

		int max1 = 0;
		int max2 = 0;

		int idx = 0;

		Collections.sort(one);

		int ans = 0;

		if (one.get(0) == 2 && one.get(1) == 4)
			ans = 2;
		else if (one.get(0) == 1 && one.get(1) == 3)
			ans = 1;
		else if (one.get(0) == 2 && one.get(1) == 3)
			ans = 3;
		else if (one.get(0) == 1 && one.get(1) == 4)
			ans = 4;

		for (int i = 0; i < 6; i++) {
			if (way[i] == one.get(0))
				max1 = len[i];

			else if (way[i] == one.get(1))
				max2 = len[i];

			if (way[i] == ans)
				idx = i;

		}

		// 큰 사각형의 넓이 구하기
		int size = max1 * max2;

		int new_idx = (idx + 2) % 6;
		int new_idx2 = (idx + 3) % 6;

		int final_size = size - (len[new_idx] * len[new_idx2]);

		System.out.println(melon * final_size);

	}

}