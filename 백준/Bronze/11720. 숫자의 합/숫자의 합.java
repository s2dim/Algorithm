import java.util.Scanner;

public class Main {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        String sinput = sc.next();
        char[] cinput = sinput.toCharArray();

        int answer = 0;

        for (int i = 0; i < cinput.length; i++) {
            answer += cinput[i] - '0';
        }

        System.out.println(answer);
        
    }

}
