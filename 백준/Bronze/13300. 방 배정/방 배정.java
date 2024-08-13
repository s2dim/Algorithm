import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		
		int student = sc.nextInt();
		int person = sc.nextInt();
		int cnt = 0;
		
		int[][] room = new int[7][2];
		for (int i = 0; i < student; i++) {
			int a = sc.nextInt();
			int b = sc.nextInt();
			
			room[b][a]++;
		}
		
		for (int i = 1; i < 7; i++) {
			for (int j = 0; j < 2; j++) {
				if (room[i][j] % person != 0) {
					cnt += (room[i][j] / person) + 1;
				} else
					cnt += (room[i][j] / person);
			}
		}
		
		System.out.println(cnt);
		
	}

}
