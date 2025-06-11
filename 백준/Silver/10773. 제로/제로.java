import java.util.Scanner;
import java.util.Stack;

public class Main {

    static Stack<Integer> stack = new Stack<>();
    static int answer = 0;

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        int k = sc.nextInt();

        for (int i = 0; i < k; i++) {
            int n = sc.nextInt();

            if (n == 0)
                stack.pop();

            else
                stack.push(n);
        }

        for (int i = 0; i < stack.size(); i++) {
            answer += stack.get(i);
        }

        System.out.println(answer);
    }
}
