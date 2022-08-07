import java.util.Scanner;
import java.util.Arrays;

public class FindingNumber {

    // 백준
    // 1920 수 찾기
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();
        int[] A = new int[N];
        for (int i = 0; i < N; i++) {
            A[i] = sc.nextInt();
        }
        Arrays.sort(A);

        int M = sc.nextInt();
        for (int i = 0; i < M; i++) {
            System.out.println(binarySearch(A, sc.nextInt()));
        }
    }

    private static int binarySearch(int[] array, int key) {
        int low = 0;
        int high = array.length - 1;

        while(low <= high) {
            int middle = (low + high) / 2;

            if (key < array[middle]) {
                high = middle - 1;
            } else if (key > array[middle]) {
                low = middle + 1;
            } else {
                return 1;
            }
        }
        return 0;
    }
}
