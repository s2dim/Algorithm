import java.util.*;

public class Main {

	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);

		int n = sc.nextInt();

		PriorityQueue<Integer> heap = new PriorityQueue<>(Collections.reverseOrder());

		for (int i = 0; i < n; i++) {
			int place = sc.nextInt();

			if (place == 0) {
				if (heap.size() == 0) {
					System.out.println("-1");
				} else {
					System.out.println(heap.poll());
				}
			} else {
				for (int j = 0; j < place; j++) {
					heap.add(sc.nextInt());
				}
			}
		}
	}

}
