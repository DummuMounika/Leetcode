class Solution {
    public int scoreOfString(String s) {
        int i = 0;
        int j = 1;
        int len = s.length();
        int res = 0;
        while (i < len && j < len)
        {
            res += Math.abs((int)s.charAt(i) - (int)s.charAt(j));
            i ++;
            j ++;
        }
        return res;
    }
}