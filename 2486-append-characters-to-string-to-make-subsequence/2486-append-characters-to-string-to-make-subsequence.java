class Solution {
    public int appendCharacters(String s, String t) {
        int lengS = s.length();
        int lengT = t.length();
        int i = 0;
        int j = 0;
        while (i < lengS && j < lengT){
            if(s.charAt(i) == t.charAt(j)){
                i++;
                j++;
            }
            else
                i++;
        }
        return lengT - j;
    }
}