import java.util.Scanner;

public class FindingNumber_TimeOut {

    // 백준
    // 1920 수 찾기
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();
        int[] A = new int[N];
        for (int i = 0; i < N; i++) {
            A[i] = sc.nextInt();
        }

        int M = sc.nextInt();
        int[] B = new int[M];
        for (int i = 0; i < M; i++) {
            B[i] = sc.nextInt();
        }

        for (int i = 0; i < M; i++) {
            boolean exists = false;
            for (int j = 0; j < N; j++) {
                if (B[i] == A[j]) {
                    exists = true;
                    System.out.println(1);
                    break;
                }
            }
            if (!exists) {
                System.out.println(0);
            }
        }
    }
}
