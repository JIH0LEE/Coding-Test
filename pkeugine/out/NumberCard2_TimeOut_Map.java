import java.util.Scanner;
import java.util.Map;
import java.util.HashMap;

public class NumberCard2_TimeOut_Map {

    // 백준
    // 10816 숫자 카드 2
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        Map<Integer, Integer> cards = new HashMap<>();
        for (int i = 0; i < N; i++) {
            int card = sc.nextInt();
            int count = cards.getOrDefault(card, 0);
            count++;
            cards.put(card, count);
        }
        int M = sc.nextInt();
        int[] results = new int[M];
        for (int i = 0; i < M; i++) {
            int card = sc.nextInt();
            System.out.print(cards.getOrDefault(card, 0) + " ");
        }
    }
}
