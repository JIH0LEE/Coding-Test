import java.util.Scanner;

// baekjun 1436
// 영화감독 숌
//
// input        output
// 2            1666
// 3            2666
// 6            5666
// 187          66666
// 500          166699
public class MovieDirectorShom {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int input = sc.nextInt();

        int number = 666;
        int count = 1;

        while (input != count) {
            number++;
            if (String.valueOf(number).contains("666")) {
                count++;
            }
        }

        System.out.println(number);
    }
}
