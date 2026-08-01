class Solution {
    private void backtrack(int nums[], int target, int startIndex, List<Integer> path, List<List<Integer>> result) {
        if (target == 0) {
            result.add(new ArrayList<Integer>(path));
            return;
        }
        for (int i=startIndex; i < nums.length; i++) {
            var n = nums[i];
            if (n > target) continue;
            path.add(n);
            this.backtrack(nums, target-n, i, path, result);
            path.remove(path.size()-1);
        }
    }
    public List<List<Integer>> combinationSum(int[] nums, int target) {
        List<List<Integer>> result = new ArrayList<>();
        this.backtrack(nums, target, 0, new ArrayList<>(), result);
        return result;
    }
}
