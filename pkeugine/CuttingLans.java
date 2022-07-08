import java.util.Scanner;
import java.util.Arrays;

// baekjun 1654
// 랜선 자르기
//
// input
// 4 11
// 802
// 743
// 457
// 539
//
// output
// 200
public class CuttingLans {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int input = sc.nextInt();
        int target = sc.nextInt();
        int[] lans = new int[input];

        long max = 0;

        for (int i = 0; i < input; i++) {
            lans[i] = sc.nextInt();
            if (max < lans[i]) {
                max = lans[i];
            }
        }

        // must be max + 1..?
        max++;

        long min = 0;
        long mid = 0;

        while (min < max) {
            mid = (min + max) / 2;

            long count = 0;

            int lansLength = lans.length;
            for (int i = 0; i < lansLength; i++) {
                count += lans[i] / mid;
            }

            if (count < target) {
                max = mid;
            } else {
                min = mid + 1;
            }
        }

        System.out.println(min - 1);
    }
}
