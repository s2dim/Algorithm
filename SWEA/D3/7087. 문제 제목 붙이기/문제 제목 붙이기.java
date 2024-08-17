import java.util.*;

public class Solution {
	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);

		int T = sc.nextInt();

		for (int t = 1; t <= T; t++) {
			int N = sc.nextInt();

			List<Integer> lst = new ArrayList<>();
			for (int i = 0; i < N; i++) {
				String str = sc.next();
				char c = str.charAt(0);
				if (c >= 65 && c < 91)
					lst.add((int) str.charAt(0));
			}

			Collections.sort(lst);

			Queue<Integer> queue = new LinkedList<>();
			for (int i = 65; i <= 65 + N; i++) {
				queue.add(i);
			}

			for (int i = 0; i < lst.size(); i++) {
				if (queue.peek() == lst.get(i)) {
					queue.poll();
				}
			}

			int x = queue.peek();
			System.out.println("#" + t + " " + (x - 65));
		}

	}
}
