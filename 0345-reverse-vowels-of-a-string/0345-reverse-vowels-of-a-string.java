class Solution {
    public boolean isVowel(char c){
        if(c=='a' || c=='e' || c=='i' || c=='o' ||c=='u' ||c=='A' || c=='E' || c=='I' || c=='O'|| c=='U')
            return true;
        else
            return false;
    }
    public String reverseVowels(String s) {
        char[] arr= s.toCharArray();
        int i = 0;
        int j = arr.length - 1;
        while (i < j){
            if(!isVowel(arr[i])){
                i++;
            }
            else if(!isVowel(arr[j])){
                j--;
            }
            else{
                char temp = arr[i];
                arr[i] = arr[j];
                arr[j] = temp;
                i++;
                j--;
            }
        }
        return String.valueOf(arr);
    }
}