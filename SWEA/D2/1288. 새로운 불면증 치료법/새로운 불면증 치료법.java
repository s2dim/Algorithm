import java.util.ArrayList;
import java.util.Scanner;

public class Solution {

	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		int T = sc.nextInt();
		
		for (int tc = 0; tc < T; tc++) {
			
			int N = sc.nextInt();
			ArrayList<Integer> list = new ArrayList<>();
			
			for (int i = 0; i <= 9; i++) {
				list.add(i);
			}
			int cnt = 0;
			
			while(true) {
				
				String str = Integer.toString(N*(cnt+1));

				for (int i = 0; i < str.length(); i++) {
					list.remove(Integer.valueOf(Character.getNumericValue(str.charAt(i))));
				}

				
				cnt++;
				if(list.size() == 0) break;
			}
			
			System.out.println("#"+(tc+1)+" "+cnt*N);
		}
		
		sc.close();
	
	}
	
}
