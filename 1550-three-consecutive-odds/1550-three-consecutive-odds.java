class Solution {
    public boolean threeConsecutiveOdds(int[] arr) {
        int oddN = 0;
        for (int i = 0;i < arr.length;i++){
            if(arr[i] % 2 != 0)
                oddN ++;
            else
                oddN = 0;
            if(oddN == 3)
                return true;
        }
        return false;
    }
}