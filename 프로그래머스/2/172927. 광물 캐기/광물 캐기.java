import java.util.*;

class Solution {
    public static int solution(int[] picks, String[] minerals) {
        int answer = 0;
        int pCount = 0;
        for (int pick : picks) pCount += pick;

        Queue<Box> q = new PriorityQueue<>((o1, o2) -> {

            if (o1.diamond != o2.diamond) {
                if (o1.diamond > o2.diamond) return -1;
                return 1;
            }
            if (o1.iron != o2.iron) {
                if (o1.iron > o2.iron) return -1;
                return 1;
            }
            if (o1.stone != o2.stone) {
                if (o1.stone > o2.stone) return -1;
                return 1;
            }
            return 0;
        });


        for(int i = 0; i < minerals.length; i+=5) {
            Box box = new Box();

            if (pCount == 0) break;
            
            for(int j = i; j < i+5; j++) {
                if (j >= minerals.length) break;
                String x = minerals[j];
                if (x.equals("diamond")) box.diamond++;
                else if (x.equals("iron")) box.iron++;
                else box.stone++;
            }
            q.add(box);
            pCount--;
        }

        while (!q.isEmpty()) {
            Box box = q.poll();
            //System.out.println("box = " + box);
            if (picks[0] > 0) {
                picks[0] --;
                answer += box.diamond;
                answer += box.iron;
                answer += box.stone;
            } else if (picks[1] > 0) {
                picks[1] --;
                answer += box.diamond * 5;
                answer += box.iron;
                answer += box.stone;
            } else if (picks[2] > 0){
                picks[2] --;
                answer += box.diamond * 25;
                answer += box.iron * 5;
                answer += box.stone;
            }
            else break;
        }

        return answer;
    }

    static class Box {
        int diamond;
        int iron;
        int stone;

        @Override
        public String toString() {
            return "Box{" +
                    "diamond=" + diamond +
                    ", iron=" + iron +
                    ", stone=" + stone +
                    '}';
        }

        public int getTotal() {
            return diamond+iron+stone;
        }
    }

}

