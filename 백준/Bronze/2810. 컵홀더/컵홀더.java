import java.util.*;

public class Main {
	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		
		int n = sc.nextInt();
		Queue<Character> queue = new LinkedList<>();
		String str = sc.next();
		boolean couple = false;
		
		for (int i = 0; i < n; i++) {
			char c = str.charAt(i);
			
			if( c == 'S') {
				queue.add('*');
				queue.add(c);
			}
			if (c == 'L') {
				if (!couple) {
					queue.add('*');
					queue.add(c);
					couple = true;
				} else {
					queue.add(c);
					couple = false;
				}
			}
		}
		queue.add('*');
		

		
		int cnt = 0;
		while (queue.size() > 2) {
			char info = queue.poll();
			if (info == '*') {
				queue.poll();
				cnt++;
			} else if (queue.peek() == '*') {
				queue.poll();
				cnt++;
			}
		}
		
		if (queue.size() == 2)
			cnt++;
		
		System.out.println(cnt);
				

	}
}
