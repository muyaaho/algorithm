import java.util.*;
import java.awt.*;

class Solution {
    public ArrayList<Integer> solution(String[] genres, int[] plays) {
        ArrayList<Integer> answer = new ArrayList<>();
        Map<String, Point> genreCount = new HashMap<>();

        for(int i = 0; i < genres.length; i++) {
            genreCount.computeIfAbsent(genres[i], key -> new Point(0, 0)).x += plays[i];
        }

        PriorityQueue<Box> q = new PriorityQueue<>((o1, o2) -> {
            if (!o1.genres.equals(o2.genres)) {
                return genreCount.get(o2.genres).x - genreCount.get(o1.genres).x;
            }if (o1.plays != o2.plays) {
                return o2.plays - o1.plays;
            }
            return o1.number - o2.number;
        });
        
        for(int i = 0; i < plays.length; i++) {
            q.offer(new Box(genres[i], plays[i], i));

        }


        while(!q.isEmpty()) {

            Box now = q.poll();
            // System.out.println(now);
            if (genreCount.get(now.genres).y < 2) {
                answer.add(now.number);
                genreCount.get(now.genres).y++;
            }
        }
        return answer;
    }

    class Box{
        String genres;
        int plays;
        int number;

        public Box (String genres, int plays, int number) {
            this.genres = genres;
            this.plays = plays;
            this.number = number;
        }

        @Override
        public String toString() {
            return "Box{" +
                    "genres='" + genres + '\'' +
                    ", plays=" + plays +
                    ", number=" + number +
                    '}';
        }
    }
}