import java.util.*;
import java.util.stream.LongStream;

class Solution {
    public long[] solution(int x, int n) {
        return LongStream.iterate((long) x, num -> num+x).limit(n).toArray();
    }
}