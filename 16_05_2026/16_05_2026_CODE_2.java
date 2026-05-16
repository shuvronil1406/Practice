//LC 7. Reverse Integer
//Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-2^31, 2^31 - 1], then return 0.

//CODE:
class Solution {
    public int reverse(int x) {
        int d;
        int res =0;
        while (x!=0){
            d = x % 10;
            if (res > 0){
                if (res > Integer.MAX_VALUE/10)
                    return (0);
                if (res == Integer.MAX_VALUE/10 && d>7)
                    return (0);
            }
            else if (res < 0){
                if (res < Integer.MIN_VALUE/10)
                    return (0);
                if (res == Integer.MIN_VALUE/10 && d < -8)
                    return (0);
            }
            res = res * 10 + d;
            x = x / 10;
        }
        return (res);
    }
}