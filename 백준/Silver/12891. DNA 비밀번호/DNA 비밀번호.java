import java.util.Arrays;
import java.util.Scanner;
import java.util.stream.IntStream;





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
		public String stringScan() {
			return scanner.nextLine();
		}
	}
	
	
	public static void main(String[] args) {

		CustomScanner scanner = new CustomScanner();
		int[] switchArr = scanner.intArrScan();

		int s = switchArr[0];
		int p = switchArr[1];
		String dna = scanner.stringScan();
		int[] needDna = scanner.intArrScan();

		int answer = 0;
		needDna = firstCheckDNA(needDna, dna, p);
		for (int i=0; i< s-p; i++) {
			if (isDNA(needDna)) {
				answer += 1;
			}
			applyNextDNA(needDna, dna, i, i+p);
		}
		if (isDNA(needDna)) {
			answer += 1;
		}
		System.out.println(answer);
	}


	private static boolean isDNA(int[] needDna) {
		for (int dna: needDna) {
			if (dna > 0) {
				return false;
			}
		}
		return true;
	}


	private static int[] firstCheckDNA(int[] needDna, String dna, int p) {
		for (int i=0; i<p; i++) {
			addNeedDNA(needDna, dna, i, -1);
		}
		return needDna;
	}


	private static void addNeedDNA(int[] needDna, String dna, int i, int n) {
		if (dna.charAt(i) == 'A') {
			needDna[0] += n;
		} else if (dna.charAt(i) == 'C') {
			needDna[1] += n;
		} else if (dna.charAt(i) == 'G') {
			needDna[2] += n;
		} else if (dna.charAt(i) == 'T') {
			needDna[3] += n;
		}
	}


	private static void applyNextDNA(int[] needDna, String dna, int i, int j) {
		addNeedDNA(needDna, dna, i, 1);
		addNeedDNA(needDna, dna, j, -1);
	}
}





