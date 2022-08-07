import java.util.Scanner;
import java.util.Arrays;
import java.util.StringJoiner;

public class NumberCard2 {

    // 백준
    // 10816 숫자 카드 2
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int[] cards = new int[N];
        for (int i = 0; i < N; i++) {
            int card = sc.nextInt();
            cards[i] = card;
        }
        Arrays.sort(cards);

        int M = sc.nextInt();
        StringJoiner sj = new StringJoiner(" ");
        for (int i = 0; i < M; i++) {
            int card = sc.nextInt();
            sj.add(String.valueOf(upperBound(cards, card) - lowerBound(cards, card)));
        }
        System.out.println(sj.toString());
    }

    private static int upperBound(int[] array, int key) {
        int low = 0;
        int high = array.length;
        while (low < high) {
            int middle = (low + high) / 2;
            if (key < array[middle]) {
                high = middle;
            } else {
                low = middle + 1;
            }
        }
        return low;
    }

    private static int lowerBound(int[] array, int key) {
        int low = 0;
        int high = array.length;
        while (low < high) {
            int middle = (low + high) / 2;
            if (key  <= array[middle]) {
                high = middle;
            } else {
                low = middle + 1;
            }
        }
        return low;
    }
}
