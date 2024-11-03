import java.util.*;

class Solution {
    public int solution(int distance, int[] rocks, int n) {
        int answer = 0;
        
        Arrays.sort(rocks);
        ArrayList<Integer> arr = new ArrayList<>();
        arr.add(0);
        for (int i = 0; i < rocks.length; i++) {
            arr.add(rocks[i]);
        }
        if (rocks[rocks.length-1] != distance) {
            arr.add(distance);
        }
        
        
        int min = 0, max = distance;
        while (min <= max) {
            int target = (min + max) / 2;
            
            
            if (check(arr, n, arr.size(), target)) {
                min = target+1;
                answer = target;
            }
            else {
                max = target - 1;
                
            }   
        }      
        return answer;
    }
    
    private boolean check(ArrayList<Integer> arr, int n, int len,  int target) {
        boolean[] deleted = new boolean[len];
        int now = 0;
        
        while (n > 0) {
            if (now + 1 >= len) {
                now = 0;
                break;
            }
            
            int next = now+1;

            while (deleted[next]) {
                next ++;
                if (next == len) {
                    now = 0;
                    next = now;
                }
            }
            
            
            int dist = arr.get(next) - arr.get(now);

            // 여기서 바위를 제거한다.
            if (dist < target) {
                n--;
                // 마지막 값은 제거할 수 없어 -> now를 제거해(마지막만)
                if (next == len-1) {
                    deleted[now] = true;
                    now = 0;
                    continue;
                }

                deleted[next] = true;

            } else {
                // 바위를 제거하지 않으면 now 업데이트 하고 그냥 넘어가야지 뭐
                now = next;
            }
        }
        
        // 바위를 제거하고도 작은거 남으면 false, 아니면 true
        
        // n이 끝나도 남은 거리가 있을 수 있음 -> now라는 건 그 앞은 조건을 만족했기 때문에 뒷부분만 확인하면 됨
        // for문 써서 past를 now로 하고 false인 부분 체크하자 그리고 for문 그대로 끝나버리면 true 리턴하고
        
        for (int next = now + 1; next < len; next++) {
            if (!deleted[next]) {
                if (arr.get(next) - arr.get(now) < target) {
                    return false;
                }
                now = next;
            }
        }
           
        // 이 모든 정보가 걸리지 않으면
        return true;
    }
    
    
}