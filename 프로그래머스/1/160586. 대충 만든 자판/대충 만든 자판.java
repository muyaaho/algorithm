class Solution {
    public int[] solution(String[] keymap, String[] targets) {
        int[] answer = new int[targets.length];
        
        for (int i = 0; i < targets.length; i++) {
            String target = targets[i];
            int cnt = 0;
            // 단어 하나씩 돌아
            for (String chr : target.split("")) {
                int idx = 100001;
                // 이제 keymap에서 작은 값 찾을거야
                for (String key : keymap) {
                    // -1이 나오면 넘어가
                    if (key.indexOf(chr) < 0) continue;
                    // 값이 나오면 min값 적용해
                    idx = Math.min(key.indexOf(chr), idx);
                }
                // -1이 나왔으면 종료해
                if (idx == 100001) {
                    cnt = -1;
                    break;
                }
                // idx가 -1이 아니면 cnt에 더해
                cnt += (idx+1);
            }
            answer[i] = cnt;
        }
        return answer;
    }
}