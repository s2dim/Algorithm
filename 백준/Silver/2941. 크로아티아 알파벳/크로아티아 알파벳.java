import java.util.*;

public class Main {
	// 2024-08-16
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		String str = sc.next();

		char[] charList = str.toCharArray();

		int sum = 0;
		for (int i = 1; i < charList.length; i++) {
			if (charList[i] == '=') {
				if (i >= 2 && charList[i - 1] == 'z' && charList[i - 2] == 'd') {
					sum++;
					charList[i] = '0';
					charList[i - 1] = '0';
					charList[i - 2] = '0';
				} else if (charList[i - 1] == 'c' || charList[i - 1] == 's' || charList[i - 1] == 'z') {
					sum++;
					charList[i] = '0';
					charList[i - 1] = '0';
				}
			} else if (charList[i] == '-') {
				sum++;
				charList[i] = '0';
				charList[i - 1] = '0';
			} else if (charList[i] == 'j') {
				if (charList[i - 1] == 'l' || charList[i - 1] == 'n') {
					sum++;
					charList[i] = '0';
					charList[i - 1] = '0';
				}
			}
		}

		for (char c : charList) {
			if (c != '0')
				sum++;
		}

		System.out.println(sum);
	}

}
