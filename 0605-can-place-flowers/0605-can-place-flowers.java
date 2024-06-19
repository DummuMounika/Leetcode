class Solution {
    public boolean canPlaceFlowers(int[] flowerbed, int n) {
        int i = 0;
        int len = flowerbed.length;
        int prev;
        int next;
        while ((i < len) && (n > 0)){
            if (flowerbed[i] == 0){
                if (i > 0)
                    prev = flowerbed[i-1];
                else
                    prev = 0;
                if (i < len -1)
                    next = flowerbed[i+1];
                else 
                    next = 0;
                if (prev == 0 && next == 0){
                    flowerbed[i] = 1;
                    n -= 1;
                }
            }
            i+=1;
        }
        if (n == 0){
            return true;
        }
        else{
            return false;
        }
           
    }
}