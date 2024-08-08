import java.util.*;
 
class Solution
{
    public static void main(String args[]) throws Exception
    {
        Scanner sc = new Scanner(System.in);
 
        int T = sc.nextInt();
 
        // 스도쿠 배열 생성
        for (int t = 1; t <= T; t++) {
            int[][] arr = new int[9][9];
            for (int i = 0; i < 9; i++) {
                for (int j = 0; j < 9; j++) {
                    arr[i][j] = sc.nextInt();
                }
            }
 
            int check = 1;
 
            // 행 계산
            for (int i = 0; i < 9; i++) {
                int[] cnt = new int[10];
                for (int j = 0; j < 9; j++) {
                    int idx = arr[i][j];
                    cnt[idx]++;
                }
                if (!(check(cnt))) {
                    check = 0;
                    break;
                }
 
            }
 
            // 열 계산
            for (int j = 0; j < 9; j++) {
                int[] cnt = new int[10];
                for (int i = 0; i < 9; i++) {
                    int idx = arr[i][j];
                    cnt[idx]++;
                }
                if (!(check(cnt))) {
                    check = 0;
                    break;
                }
            }
 
            // 9칸
            for (int r = 0; r < 3; r++) {
                for (int c = 0; c < 3; c++) {
                    int[] cnt = new int[10];
//                  System.out.println("---");
                    for (int i = r * 3; i < (r * 3) + 3; i++) {
                        for (int j = c * 3; j < (c * 3) + 3; j++) {
                            int idx = arr[i][j];
                            cnt[idx]++;
                        }
                    }
                    if (!(check(cnt))) {
                        check = 0;
                        break;
                    }
                }
                if (check == 0) break; // gpt 추가
            }
            System.out.println("#" + t + " " + check);
        }
    }
 
    static boolean check(int[] cnt) {
 
        for (int i = 1; i <= 9; i++) {
            if (cnt[i] == 0)
                return false;
        }
        return true;
    }
}