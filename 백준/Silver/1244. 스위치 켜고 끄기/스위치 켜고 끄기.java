import java.util.Arrays;
import java.util.Scanner;





public class Main {
	private static class CustomScanner {
		Scanner scanner = new Scanner(System.in);
		
		public int intScan() {
			String input = scanner.nextLine();
			return Integer.parseInt(input);
		}
		public int[] intArrScan() {
			String input = scanner.nextLine();
			int[] intArr = Arrays.stream(input.split(" ")).mapToInt(Integer::parseInt).toArray();
			return intArr;
		}	
	}

	
	
	private static int change(int x) {
		if (x==1) {
			return 0;
		}
		return 1;
	}
	
	public static void main(String[] args) {

		CustomScanner scanner = new CustomScanner();
		int switchN = scanner.intScan();
		int[] switchArr = scanner.intArrScan();
		int studentN = scanner.intScan();

		for (int i=0; i < studentN; i++) {
			int[] student_arr = scanner.intArrScan();
			if (student_arr[0] == 1) {
				// do boy's job
				int j = 1;
				while (true) {
					int nextN = j * student_arr[1]; // boy's switch
					if (nextN - 1 >= switchN) {
						break;
					}
					switchArr[nextN -1] = change(switchArr[nextN -1]);
					j += 1;
				}
			} else {
				// do girl's job
				int j = 0;
				while (true) {
					int next_left_n = student_arr[1] - j;
					int next_right_n = student_arr[1] + j;
					if (next_left_n - 1 < 0 || next_right_n - 1 >= switchN) {
						break;
					}
					if (j == 0) {
						switchArr[student_arr[1] - 1] = change(switchArr[student_arr[1] - 1]);
					} else if (switchArr[next_left_n -1] == switchArr[next_right_n -1]){
						switchArr[next_left_n -1] = change(switchArr[next_left_n -1]);
						switchArr[next_right_n -1] = change(switchArr[next_right_n -1]);		
					} else {
						break;
					}
					j += 1;
				}
			}
		}
		
		for (int i=1; i<=switchN; i++) {
			if (i % 20 == 0) {
				System.out.printf("%d\n", switchArr[i - 1]);
			} else {
				System.out.printf("%d ", switchArr[i - 1]);
			}
		}
		
	}
}
