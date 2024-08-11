import java.math.BigInteger;

class Solution {
        public static BigInteger solution(int n) {

        BigInteger[] array = new BigInteger[n+1];

        array[0] = BigInteger.valueOf(0);
        array[1] = BigInteger.valueOf(1);


        for(int i=2;i<=n;i++){
//            array[i-1].add(array[i-2]);
            array[i] =   array[i-1].add(array[i-2]);
        }

//        System.out.println(Arrays.toString(array));
        BigInteger a= array[n].remainder(BigInteger.valueOf(1234567));
        return a;
    }
}