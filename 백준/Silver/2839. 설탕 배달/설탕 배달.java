import java.util.*;

public class Main {

	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);

		int sugar = sc.nextInt();
		
		int max = sugar / 3 + 1;
		
		int min = max;
		
		for (int i = 0; i < max; i++) {
			for (int j = 0; j < max; j++) {
				if (5 * i + 3 * j == sugar) {
					min = Math.min(i+j, min);
				}
			}
		}
		
		if (min == max) {
			min = -1;
		}
		System.out.println(min);
	}

}
