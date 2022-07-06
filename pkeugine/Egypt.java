import java.util.Scanner;

// baekjun 4153
// Egypt (직각 삼각형)
//
// input              output
// 6 8 10             right
// 25 52 60           wrong
// 5 12 13            right
// 0 0 0              (program finished)
public class Egypt {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        while (true) {
            int a = sc.nextInt();
            int b = sc.nextInt();
            int c = sc.nextInt();
            if (a == 0 && b == 0 && c == 0) {
                break;
            }

            a = a * a;
            b = b * b;
            c = c * c;

            if (a == b + c || b == a + c || c == a + b) {
                System.out.println("right");
            } else {
                System.out.println("wrong");
            }
        }
    }
}
