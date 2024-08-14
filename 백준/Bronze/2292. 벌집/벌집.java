import java.util.*;

public class Main {
	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		
		int lastN = 1;
		int room = 1;
		
		while (n > lastN) {
			
			lastN = lastN + 6 * room; 
			room ++;
		}
		
		System.out.println(room);
	}
	

}
