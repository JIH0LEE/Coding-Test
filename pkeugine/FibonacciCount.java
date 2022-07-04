import java.util.Scanner;

public class FibonacciCount {

    private int[] fibo;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Main main = new Main();

        System.out.println("enter the input (ex: 10)
        int n = sc.nextInt();
        main.solution(n);
    }

    private void solution(int n) {
        System.out.println(first(n) + " " + second(n));
    }

    private int first(int n) {
        fibo = new int[n];
        fibo[0] = 1;
        fibo[1] = 1;
        for (int i = 2; i < n; i++) {
            fibo[i] = fibo[i-1] + fibo[i-2];
        }
        return fibo[n-1];
    }

    private int second(int n) {
        // 5 <= n <= 40
        // return n > 2 ? n - 2 : 0;
        return n - 2;
    }
}
