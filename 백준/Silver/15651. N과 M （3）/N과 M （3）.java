import java.util.Scanner;

public class Main {
	
	static int[] arr;
	static StringBuilder sb = new StringBuilder();
	
	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		
		int n = sc.nextInt();
		int m = sc.nextInt();
		
		arr = new int[m];
		
		cal(n, m, 0);
		System.out.println(sb);

	}
	
	static void cal(int n, int m, int depth) {
		
		if (depth == m) {
			for (int i : arr) {
				sb.append(i).append(" ");
			}
			sb.append("\n");
			return;
		}
		
		for (int i = 0; i < n; i++) {
			arr[depth] = i + 1;
			cal(n, m, depth + 1);
		}
	}

}
