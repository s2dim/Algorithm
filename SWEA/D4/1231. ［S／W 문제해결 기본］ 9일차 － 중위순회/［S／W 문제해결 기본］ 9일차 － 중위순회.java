import java.util.*;

public class Solution {
	private static String[] tree;
    private static String inOrderTest = "";
	
	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);


		// 10개 테스트 케이스
		for (int t = 1; t <= 10; t++) {
			int n = sc.nextInt();
			sc.nextLine();
			
			tree = new String[n+1];
			
			for (int i = 1; i <= n; i++) {

				// 정점 번호
				int num = sc.nextInt();
				// 알파벳
				String word = sc.next();
				sc.nextLine();
				
				tree[num] = word;
				


			}
			
			inOrder(1);
			System.out.println("#" + t + " " + inOrderTest);
			inOrderTest = "";
		}
	}
	
    private static void inOrder(int index) {
        if (index >= tree.length || tree[index] == "") {
            return;
        }
        
       
        inOrder(index*2);
        inOrderTest += tree[index];
        inOrder(index*2+1);

    }
}