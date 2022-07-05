import java.util.Scanner;

// baekjun 1912
public class ContinuousSum {

    private int[] numbers;

    public static void main(String[] args) {
        Main main = new Main();
        main.solution();
    }

    private void solution() {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        numbers = new int[n];

        // minimum input is -1000
        int max = -1001;
        for (int i = 0; i < n; i++) {
            int k = sc.nextInt();

            if (i == 0) {
                max = k;
                numbers[i] = k;
                continue;
            }
            // numbers[i-1] + k
            // k
            numbers[i] = Math.max(numbers[i-1] + k, k);
            // if (numbers[i] < numbers[i-1]) {
            //    numbers[i] = 0;
            //}
            if (max < numbers[i]) {
                max = numbers[i];
            }
        }

        System.out.println(max);
    }
}
