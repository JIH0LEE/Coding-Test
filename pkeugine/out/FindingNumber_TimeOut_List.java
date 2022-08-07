import java.util.Scanner;
import java.util.List;
import java.util.ArrayList;

public class FindingNumber_TimeOut_List {

    // 백준
    // 1920 수 찾기
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();
        List<Integer> A = new ArrayList<>();
        for (int i = 0; i < N; i++) {
            A.add(sc.nextInt());
        }

        int M = sc.nextInt();
        for (int i = 0; i < M; i++) {
            if (A.contains(sc.nextInt())) {
                System.out.println(1);
            } else {
                System.out.println(0);
            }
        }
    }
}
