import java.util.Arrays;
import java.util.Scanner;
import java.util.Stack;

public class Main {
	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);

		String str = sc.nextLine();
		int len = str.length();
		char[] c = str.toCharArray();
		Stack<Character> stack = new Stack<>();

		StringBuilder sb = new StringBuilder();

		int idx = 0;

		while (idx < len) {

			if (c[idx] == '<') {
				while (!stack.isEmpty()) {
					char popItem = stack.pop();
					sb.append(popItem);
				}
				while (c[idx] != '>') {
					sb.append(c[idx]);
					idx++;
				}
				sb.append(c[idx]);
				idx++;

			} else if (c[idx] == ' ') {
				while (!stack.isEmpty()) {
					char popItem = stack.pop();
					sb.append(popItem);
				}
				sb.append(c[idx]);
				idx++;
			} else {

				stack.add(c[idx]);
				idx++;

			}
		}

		if (!stack.isEmpty()) {
			while (!stack.isEmpty()) {
				char popItem = stack.pop();
				sb.append(popItem);
			}
		}

		System.out.println(sb);
	}
}