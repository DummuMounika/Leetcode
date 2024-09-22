class NumArray {
    int[] preSum;
    public NumArray(int[] nums) {
        preSum = nums;
        for(int i = 1;i < preSum.length; i++){
            System.out.println("eee:" +preSum[i]);
            preSum[i] += preSum[i-1];
        }     
    }
    
    public int sumRange(int left, int right) {
        if (left == 0){
            return preSum[right];
        }
        int pSum = preSum[right] - preSum[left-1];
        return pSum;    
    }
}

/**
 * Your NumArray object will be instantiated and called as such:
 * NumArray obj = new NumArray(nums);
 * int param_1 = obj.sumRange(left,right);
 */