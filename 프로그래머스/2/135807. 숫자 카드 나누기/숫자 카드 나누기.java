class Solution {
    public int solution(int[] arrayA, int[] arrayB) {
        int answer = 0;
        int a = func(arrayA);
        int b = func(arrayB);
        
        boolean divA = isDiv(arrayB, a);
        boolean divB = isDiv(arrayA, b);
        
        if (divA && divB) answer = 0;
        else if (!divA && !divB) answer = a > b ? a : b;
        else {
            if (divA) answer = b;
            else answer = a;
        }
        
        return answer;
    }
    
    private boolean isDiv(int[] arr, int x) {
        if (x == 0) return true;
        for (int i = 0; i < arr.length; i++) {
            if (arr[i] % x == 0) return true;
        }
        return false;
    }
    
    private int func(int[] arr) {
        int x = arr[0];
        if (arr.length == 1) return x;
        
        for (int i = 1; i < arr.length; i++) {
            if (x == 1) return 0;
            
            x = gcd(arr[i], x);
        }
        
        return x;
    } 
    
    private int gcd (int a, int b) {
        while (b != 0) {
            int tmp = a % b;
            a = b;
            b = tmp;
        }
        return a;
    }
}