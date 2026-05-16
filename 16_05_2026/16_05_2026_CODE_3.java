//LC 9. Pallindrome Number

//Given an integer x, return true if x is a palindrome, and false otherwise.

//CODE:

class Solution {
    public boolean isPalindrome(int x) {
        if (x < 0){
            return false;
        }
        Reverse obj = new Reverse();
        int res;
        res = obj.reverse(x);
        if (res == x){
           return (true);
        }
        return (false);

    }
}
class Reverse{
    public int reverse(int x){
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
            res = res * 10 + d;
            x = x / 10;
        }
        return (res);
    }
}