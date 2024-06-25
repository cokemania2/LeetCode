import java.util.Scanner;

public class Main {
    public static boolean isPossible(int[] arr, int depth, int column) {
        for (int i = 0; i < depth; i++) {
            // 같은 열에 있는지 확인
            if (arr[i] == column) {
                return false;
            }
            // 대각선에 있는지 확인
            if (Math.abs(depth - i) == Math.abs(column - arr[i])) {
                return false;
            }
        }
        return true;
    }

    public static int nQueen(int depth, int n, int[] arr) {
        if (depth == n) {
            return 1;
        }
        int answer = 0;
        for (int column = 0; column < n; column++) {
            if (isPossible(arr, depth, column)) {
                arr[depth] = column;
                answer += nQueen(depth + 1, n, arr);
                arr[depth] = -1;
            }
        }
        return answer;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = -1;
        }
        System.out.println(nQueen(0, n, arr));
    }
}