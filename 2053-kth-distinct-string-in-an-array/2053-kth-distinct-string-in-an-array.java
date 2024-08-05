class Solution {
    public String kthDistinct(String[] arr, int k) {
        Map<String, Integer> stringFreq = new HashMap<>();
        for(String str: arr) {
            stringFreq.put(str, stringFreq.getOrDefault(str, 0)+1);
        }
        for(String str: arr) {
            if (stringFreq.get(str) == 1)
                k--;
            if (k == 0)
                return str;
        }
        return "";
    }
}