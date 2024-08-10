import java.util.*;

public class Solution {
	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);

		int T = sc.nextInt();

		for (int t = 1; t <= T; t++) {
			int n = sc.nextInt();
			sc.nextLine();
			
			char[][] arr = new char[n][n];

			List<Integer> lst = new ArrayList<>();

		       for (int i = 0; i < n; i++) {
		    	   String str = sc.nextLine();   
		            String[] strArr = str.split(" "); 

		            for (int j = 0; j < n; j++) {
		                arr[i][j] = strArr[j].charAt(0); 
		            }
		        }

			for (int i = 1; i < n - 1; i++) {
				for (int j = 1; j < n - 1; j++) {
					int sum = 0;
					if (arr[i - 1][j - 1] == 'W')
						sum++;
					if (arr[i - 1][j] == 'W')
						sum++;
					if (arr[i - 1][j + 1] == 'W')
						sum++;
					if (arr[i][j - 1] == 'W')
						sum++;
					if (arr[i][j + 1] == 'W')
						sum++;
					if (arr[i + 1][j - 1] == 'W')
						sum++;
					if (arr[i + 1][j] == 'W')
						sum++;
					if (arr[+1][j + 1] == 'W')
						sum++;
					lst.add(sum);
				}
			}

			Collections.sort(lst, Collections.reverseOrder());

			int max = lst.get(0);

			if (max == 0) {
				max = 1;
			}
			System.out.println("#" + t + " " + max);
		}

	}
}
