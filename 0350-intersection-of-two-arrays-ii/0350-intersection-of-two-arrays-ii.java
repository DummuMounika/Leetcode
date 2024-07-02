class Solution {
    public int[] intersect(int[] nums1, int[] nums2) {
        List<Integer> repL = new ArrayList<>();
        HashMap<Integer , Integer> dictN = new HashMap<>();

        for(int num1: nums1){
            dictN.put(num1, dictN.getOrDefault(num1, 0) + 1);
        }
        for(int num2: nums2){
            if(dictN.containsKey(num2) && dictN.get(num2) > 0){
                repL.add(num2);
                dictN.put(num2, dictN.get(num2)-1);
            }
        }
        int [] resArray = new int[repL.size()];
        for(int i=0;i<repL.size();i++){
            resArray[i] = repL.get(i);
        }
        return resArray;

        
    }
}