import java.util.*;

class Solution {
    public boolean solution(String[] phone_book) {
        Arrays.sort(phone_book);
        
        boolean flag = false;
        for (int i = 0; i < phone_book.length-1; i++) {
            for (int j = i+1; j < phone_book.length; j++) {
                
                if (phone_book[j].indexOf(phone_book[i]) == 0)
                    return false;
                else 
                    break;
                
            }
        }

        return true;
    }
}