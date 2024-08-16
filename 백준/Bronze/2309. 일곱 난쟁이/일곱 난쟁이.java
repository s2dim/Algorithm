import java.util.*;

public class Main {

	public static void main(String[] args) {

		List<Integer> lst = new ArrayList<>();
		Scanner sc = new Scanner(System.in);

		int sum = 0;
		for (int i = 0; i < 9; i++) {
			int cm = sc.nextInt();
			lst.add(cm);
			sum += cm;
		}
		
		int a = 0;
		int b = 0;
		int minus = sum - 100;
		
		System.out.println();

		xx: for (int i = 0; i < 8; i++) {
			for (int j = i + 1; j < 9; j++) {

				if (lst.get(i) + lst.get(j) == minus) {
					a = i;
					b = j;
					break xx;
				}

			}
		}

		lst.remove(b);
		lst.remove(a);

		Collections.sort(lst);
		
		for (Integer integer : lst) {
			System.out.println(integer);
		}
	}

}
