import java.util.*;

public class Main {

	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);

		int n = sc.nextInt();
		int m = sc.nextInt();

		List<Integer> lst = new ArrayList<>();

		for (int i = 0; i < n; i++) {
			lst.add(sc.nextInt());
		}

		Collections.sort(lst);

		if (lst.get(0) + lst.get(1) + lst.get(lst.size() - 1) >= m) {
			lst.remove(lst.size() - 1);
		}

		System.out.println(combination(lst, m));

	}

	static int combination(List<Integer> lst, int m) {
		int len = lst.size();

		List<Integer> sumList = new ArrayList<>();

		for (int i = 0; i < lst.size() - 2; i++) {
			for(int j = i + 1; j < lst.size() - 1; j++) {
				for (int k = i + 2; k < lst.size(); k++) {
					int sum = lst.get(i) + lst.get(j) + lst.get(k);
					if (sum <= m)
					sumList.add(sum);
					
				}
			}
		}
		
		Collections.sort(sumList, Collections.reverseOrder());
		
		return sumList.get(0);
	
		}

	}
