

import java.util.*;

public class Main {
	
	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		
		int n = sc.nextInt();
		
		PriorityQueue<Integer> heap = new PriorityQueue<>();
		
		for (int i = 0; i < n; i++) {
			int x = sc.nextInt();
			if (x != 0) {
				heap.add(x);
			} else if (x == 0 & heap.size() != 0) {
				System.out.println(heap.poll());
			} else if (x == 0 && heap.size() == 0) {
				System.out.println(0);
			}
		}
	}

}
