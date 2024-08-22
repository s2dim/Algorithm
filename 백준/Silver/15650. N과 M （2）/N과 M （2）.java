
import java.util.Scanner;

public class Main {

	static int[] arr;
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		int n = sc.nextInt();
		int m = sc.nextInt();
		
		arr = new int[m];
		
		cal(n, m, 0, 0);
		
	}
	
	static void cal(int n, int m, int start, int depth) {
		
		if (depth == m) {
			for (int i : arr) {
				System.out.print(i + " ");
			}
			System.out.println();
			return;
		}
		
		for (int i = start; i < n; i++) {
			
				

				arr[depth] = i + 1;
				cal(n, m, i + 1, depth+1);
				
			}
		return;
	}
}
