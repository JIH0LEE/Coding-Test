public class PEShirt {

    public static void main(String[] args) {
        Solution solution = new Solution();

        // 5
        int[] firstLost = {2,4};
        int[] firstReserve = {1,3,5};
        System.out.println(solution.solution(5, firstLost, firstReserve));
        // 4
        int[] secondLost = {2,4};
        int[] secondReserve = {3};
        System.out.println(solution.solution(5, secondLost, secondReserve));
        // 2
        int[] thirdLost = {3};
        int[] thirdReserve = {1};
        System.out.println(solution.solution(3, thirdLost, thirdReserve));
    }
}

class Solution {

    public int solution(int n, int[] lost, int[] reserve) {
        int[] count = new int[n];
        boolean[] possible = new boolean[n];
        for (int i = 0; i < n; i++) {
            if (arrayContains(reserve, i + 1)) {
                count[i] = 2;
            } else {
                count[i] = 1;
            }
            if (arrayContains(lost, i + 1)) {
                count[i]--;
            }
        }
        for (int i = 0; i < n; i++) {
            if (count[i] > 0) {
                possible[i] = true;
                continue;
            }

            if (i == 0) {
                if (count[1] == 2) {
                    count[1]--;
                    count[0]++;
                    possible[0] = true;
                }
                continue;
            }

            if (i == n-1) {
                if (count[n-2] == 2) {
                    count[n-2]--;
                    count[n-1]++;
                    possible[n-1] = true;
                }
                continue;
            }

            if (count[i-1] == 2) {
                count[i-1]--;
                count[i]++;
                possible[i] = true;
                continue;
            }

            if (count[i+1] == 2) {
                count[i+1]--;
                count[i]++;
                possible[i] = true;
                continue;
            }
        }

        int answer = 0;
        for (int i = 0; i < n; i++) {
            if (possible[i] == true) {
                answer++;
            }
        }
        return answer;
    }

    private boolean arrayContains(int[] array, int k) {
        for (int num : array) {
            if (num == k) {
                return true;
            }
        }
        return false;
    }
}
