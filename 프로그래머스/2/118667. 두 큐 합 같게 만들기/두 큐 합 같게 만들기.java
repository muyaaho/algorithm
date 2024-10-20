class Solution {
    long sumAll;
    int[] addArr;
    public int solution(int[] queue1, int[] queue2) {

        int size = queue1.length;
        int answer = Integer.MAX_VALUE;

        addArr = new int[size * 2];
        for (int i = 0; i < size * 2; i++) {
            if (i < size) {
                addArr[i] = queue1[i];
                sumAll += queue1[i];
            } else {
                addArr[i] = queue2[i - size];
                sumAll += queue2[i - size];
            }
        }

        int start = 0, end = size;

        long s = 0L;
        for (int i = start; i < end; i++) {
            s += addArr[i];
        }
        
        while (start <= end) {
//             System.out.println("start=" + start + ", end=" + end);
//             System.out.println("s=" + s);
            if (s == sumAll/2) {
                answer = start + (end - size);
                break;
            }
            
            if (end + 1 < addArr.length && s < sumAll/2) {
                s += addArr[end];
                end++;
            } else {
                s -= addArr[start];
                start++;
            }
        }
        return answer == Integer.MAX_VALUE ? -1 : answer;
    }
}