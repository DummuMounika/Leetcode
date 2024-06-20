class Solution {
    public int compress(char[] chars) {
        int i = 0;
        int newIndex = 0;
        int charsL = chars.length;

        while(i < charsL){
            final char charV = chars[i];
            int count = 0;
            while (i < charsL && chars[i] == charV){
                count++;
                i++;
            }
            chars[newIndex] = charV;
            newIndex++;

            if(count > 1) {
                for (final char c : String.valueOf(count).toCharArray()){
                    chars[newIndex] = c;
                    newIndex++;
                }
            }
        }
        return newIndex;
        
    }
}