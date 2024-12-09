

import java.util.Scanner;

public class Main {
	
	static int n, m;
	static boolean visited[];
	static int[] arr;
	
	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		
		n = sc.nextInt();
		m = sc.nextInt();
		
		visited = new boolean[n];
		arr = new int[m];
		
		cal(0);
		
	}
	
	static void cal(int depth) {
		
		if (depth == m) {
			for (int i = 0; i < m; i++) {
				System.out.print(arr[i] + " ");
			}
			System.out.println();
			return;
		}
		
		for (int i = 0; i < n; i++) {
			if (!visited[i]) {
				visited[i] = true;
				arr[depth] = i + 1;
				cal(depth + 1);
				visited[i] = false;
			}
		}
	}

}
