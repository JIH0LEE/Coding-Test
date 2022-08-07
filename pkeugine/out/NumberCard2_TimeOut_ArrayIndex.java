import java.util.Scanner;

public class NumberCard2_TimeOut_ArrayIndex {

    // 백준
    // 10816 숫자 카드 2
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        // 0 1~10000000 -1~-10000000(10000001 ~ 20000000)
        int[] cards = new int[20000001];
        for (int i = 0; i < N; i++) {
            int card = sc.nextInt();
            if (card < 0) {
                card = (card * -1) + 10000000;
            }
            cards[card]++;
        }
        int M = sc.nextInt();
        for (int i = 0; i < M; i++) {
            int card = sc.nextInt();
            if (card < 0) {
                card = (card * -1) + 10000000;
            }
            System.out.print(cards[card] + " ");
        }
    }
}
