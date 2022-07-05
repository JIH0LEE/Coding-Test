import java.util.Arrays;

// 프로그래머스
// 전화번호 목록
public class PhoneBook {

    public static void main(String[] args) {
        Solution solution = new Solution();

        // false
        String[] firstPhoneBook = {"119", "97674223", "1195524421"};
        System.out.println(solution.solution(firstPhoneBook));

        // true
        String[] secondPhoneBook = {"123","456","789"};
        System.out.println(solution.solution(secondPhoneBook));

        // false
        String[] thirdPhoneBook = {"12","123","1235","567","88"};
        System.out.println(solution.solution(thirdPhoneBook));
    }
}

class Solution {

    public boolean solution(String[] phone_book) {
        Arrays.sort(phone_book);
        int length = phone_book.length;

        for (int i = 0; i < length - 1; i++) {
            if (phone_book[i + 1].startsWith(phone_book[i])) {
                return false;
            }
        }

        return true;
    }
}
