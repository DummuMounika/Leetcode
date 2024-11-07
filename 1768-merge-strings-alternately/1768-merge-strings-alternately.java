class Solution {
    public String mergeAlternately(String word1, String word2) {
        StringBuilder newStr = new StringBuilder();
        int i = word1.length();
        int j = word2.length();
        for(int n = 0; n < Math.max(i,j); n++){
            if (n < i )
                newStr.append(word1.charAt(n));
            if (n < j)
                newStr.append(word2.charAt(n));
        }
        return newStr.toString();
    }
}