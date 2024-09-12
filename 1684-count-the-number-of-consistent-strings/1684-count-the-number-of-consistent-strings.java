class Solution {
    public boolean check(String word,String al){
        for(char ch: word.toCharArray()) {
            if(al.indexOf(ch) == -1){
                return false;
            }
        }
        return true;
    }
    public int countConsistentStrings(String allowed, String[] words) {
        int count = 0;
        for(String word:words){
            if(check(word,allowed)) {
                count ++;
            }
        }
        return count;
        
    }
}