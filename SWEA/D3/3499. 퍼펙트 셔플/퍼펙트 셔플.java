import java.util.*;

class Solution
{
	public static void main(String args[]) throws Exception
	{
		Scanner sc = new Scanner(System.in);
		
		int T = sc.nextInt();
		
		for (int t = 1; t <= T; t++) {
			int n = sc.nextInt();
			
			Queue<String> queue1 = new LinkedList<>();
			Queue<String> queue2 = new LinkedList<>();
			
			StringBuilder res = new StringBuilder();
			
			for (int i = 0; i < n; i+=2) {
				String s = sc.next();
				queue1.add(s);
			}
			
			for (int i = 1; i < n; i+=2) {
				String s = sc.next();
				queue2.add(s);
			}
			
			for (int i = 0; i < (n / 2) + 1; i++) {
				
				if(queue1.isEmpty()){
					continue;
				} 
				res.append(queue1.poll());
				res.append(" ");
				
				if (queue2.isEmpty()) {
					continue;
				}
				res.append(queue2.poll());
				res.append(" ");
				
			}
			
			System.out.println("#" + t + " " + res);
		}
	}

}