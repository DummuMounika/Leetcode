class Solution {
    public String compressedString(String word) {

        StringBuilder res = new StringBuilder();
        int count = 1;

        for (int i = 1; i < word.length(); i++) {     
            if (word.charAt(i) == word.charAt(i - 1)) {
                if (count == 9) {  
                    res.append(count).append(word.charAt(i - 1));
                    count = 1;
                }else{
                    count++;
                }
            } else {
                res.append(count).append(word.charAt(i - 1));
                count = 1;
            }
        }
        res.append(count).append(word.charAt(word.length() - 1));
        return res.toString();
    }
}
