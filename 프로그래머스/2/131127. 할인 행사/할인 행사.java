import java.util.*;
class Solution {
    public int solution(String[] want, int[] number, String[] discount) {
        int answer = 0;
        Map<String, Integer> check = initMap(want, number);

        for (int i = 0; i < discount.length - 10 + 1; i++) {
            // System.out.println("i = " + i);
            for (int k = i; k < i + 10; k++) {
                // check에 포함되지 않으면 종료
                String x = discount[k];
                if (!check.containsKey(x)) {
                    break;
                }
                // check에 포함되면 check값 하나씩 빼기
                check.put(x, check.get(x) - 1);
            }
            // 모든 value가 0인지 확인
            if (checkZero(want, check)) {
                answer ++;
            }
            check = initMap(want, number);
        }

        return answer;
    }

    private static boolean checkZero(String[] want, Map<String, Integer> check) {
        for (String s : want) {
            if(check.get(s) != 0) {
                return false;
            }
        }
        return true;
    }

    private static Map<String, Integer> initMap(String[] want, int[] number) {
        Map<String, Integer> check = new HashMap<>();
        for (int i = 0; i < want.length; i++) {
            check.put(want[i], number[i]);
        }
        return check;
    }
}