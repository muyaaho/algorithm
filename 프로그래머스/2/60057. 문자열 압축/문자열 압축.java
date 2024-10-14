class Solution {
    public int solution(String s) {
        if (s.length() == 1) return 1;
        int answer = Integer.MAX_VALUE;
        
        for (int cut = 1; cut <= s.length() / 2; cut++) {
            int index = 0;
            StringBuilder sb = new StringBuilder();
            
            while (cut <= s.length() - index) {
                int count = 0;
                String str = s.substring(index, index + cut);
                while (index + cut <= s.length() && str.equals(s.substring(index, index+cut))) {
                    count ++;
                    index += cut;
                }
                if (count > 1) {
                    sb.append(count);
                }
                sb.append(str);
                
            }
            sb.append(s.substring(index));
            answer = Math.min(answer, sb.length());
        }
        return answer;
    }
}