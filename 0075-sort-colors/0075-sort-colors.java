class Solution {
    public void sortColors(int[] nums) {
        int low = 0;
        int high = nums.length -1;
        int mid = 0;
        while (mid <= high){
            if (nums[mid] == 0){
                int temp1 = nums[low];
                int temp2 = nums[mid];
                nums[low] = temp2;
                nums[mid] = temp1;
                low ++;
                mid ++;
            }
            else if(nums[mid] == 2){
                int temp1 = nums[high];
                int temp2 = nums[mid];
                nums[high] = temp2;
                nums[mid] = temp1;
                high --;
            }else
                mid ++;
        }   
    }
}