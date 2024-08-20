import java.util.*;

public class Main {
	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);
		int num = sc.nextInt();
		System.out.println(factorial(num));
		
	}

	static long factorial(int num) {
		if (num > 1) {
			return factorial(num - 1) * num;
		} else {
			return 1;
		}
	}
}
