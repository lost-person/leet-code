import java.util.List;
import java.util.Arrays;
import java.util.LinkedList;

/*
 * @lc app=leetcode id=18 lang=java
 *
 * [18] 4Sum
 *
 * https://leetcode.com/problems/4sum/description/
 *
 * algorithms
 * Medium (29.59%)
 * Total Accepted:    210.1K
 * Total Submissions: 710.1K
 * Testcase Example:  '[1,0,-1,0,-2,2]\n0'
 *
 * Given an array nums of n integers and an integer target, are there elements
 * a, b, c, and d in nums such that a + b + c + d = target? Find all unique
 * quadruplets in the array which gives the sum of target.
 * 
 * Note:
 * 
 * The solution set must not contain duplicate quadruplets.
 * 
 * Example:
 * 
 * 
 * Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.
 * 
 * A solution set is:
 * [
 * ⁠ [-1,  0, 0, 1],
 * ⁠ [-2, -1, 1, 2],
 * ⁠ [-2,  0, 0, 2]
 * ]
 * 
 * 
 */
class Solution {
    public List<List<Integer>> fourSum(int[] nums, int target) {
        Arrays.sort(nums);
        return kSum(nums, 0, nums.length - 1, target, 4);
    }

    public List<List<Integer>> kSum(int[] nums, int start, int end, int target, int k){
        List<List<Integer>> list = new LinkedList<>();
        if(k == 2){
            while(start < end){
                if(nums[start] + nums[end] == target){
                    list.add(new LinkedList<Integer>(Arrays.asList(nums[start], nums[end])));
                    // 避免重复计算
                    while(start < end && nums[start + 1] == nums[start]) start++;
                    while(start < end && nums[end - 1] == nums[end]) end--;
                    start++;
                    end--;
                }
                else if(nums[start] + nums[end] < target) start++;
                else end--;
            }
        }
        else{
            int i = start;
            for(; i < nums.length - k + 1 && nums[i] * k <= target; i++){
                if(i > start && nums[i] == nums[i - 1]) continue;
                List<List<Integer>> resList = kSum(nums, i + 1, nums.length - 1, target - nums[i], k - 1);
                for(List<Integer> tmpList : resList)
                    tmpList.add(0, nums[i]);
                list.addAll(resList);
            }
        }
        return list;
    }
}
