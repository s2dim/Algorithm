import java.util.*;

public class Main {
	// 2024-08-15
	
	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		
		Set<Integer> set = new HashSet<>();
		
		for (int t = 0; t < 10; t++) {
			int n = sc.nextInt();
			
			set.add(n % 42);
		}
		
		System.out.println(set.size());
	}
}
