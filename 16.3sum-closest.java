import java.util.Arrays;
/*
 * @lc app=leetcode id=16 lang=java
 *
 * [16] 3Sum Closest
 *
 * https://leetcode.com/problems/3sum-closest/description/
 *
 * algorithms
 * Medium (37.43%)
 * Total Accepted:    261.4K
 * Total Submissions: 698.5K
 * Testcase Example:  '[-1,2,1,-4]\n1'
 *
 * Given an array nums of n integers and an integer target, find three integers
 * in nums such that the sum is closest to target. Return the sum of the three
 * integers. You may assume that each input would have exactly one solution.
 * 
 * Example:
 * 
 * 
 * Given array nums = [-1, 2, 1, -4], and target = 1.
 * 
 * The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
 * 
 * 
 */
class Solution {
    public int threeSumClosest(int[] nums, int target) {
    //     // 方法1
    //     int ans;
    //     // 差值
    //     int diff = 0;
    //     Arrays.sort(nums);
    //     int i = 0;

    //     // 通过三数求和求出最接近的值
    //     while(true){
    //         if(kSum(nums, 0, nums.length - 1, target + diff, 3)){
    //             ans = target + diff;
    //             break;
    //         }
    //         if(diff != 0)
    //             if(kSum(nums, 0, nums.length - 1, target - diff, 3)){
    //                 ans = target - diff;
    //                 break;
    //             }
                    
    //         diff++;
    //     }
    //     return ans;
    // }

    // // 三数求和
    // public boolean kSum(int[] nums, int start, int end, int target, int k){
    //     if(k == 2){
    //         while(start < end){
    //             if(nums[start] + nums[end] == target) return true;
    //             else if(nums[start] + nums[end] < target) start++;
    //             else end--;
    //         }
    //     }
    //     else{
    //         int i = start;
    //         for(; i < nums.length - k + 1 && nums[i] * k <= target; i++){
    //             // 避免重复计算
    //             if(i > start && nums[i] == nums[i - 1]) continue;
    //             if(kSum(nums, i + 1, nums.length - 1, target - nums[i], k - 1))
    //                 return true;
    //         }
    //     }
    //     return false;
    // }

    // 方法2
    Arrays.sort(nums);
    int result = nums[0] + nums[1] + nums[2];
    int sum;
    for (int i = 0; i < nums.length - 2; i++) {
        int j = i + 1, k = nums.length - 1;
        while (j < k) {
            sum = nums[i] + nums[j] + nums[k];
            if (sum == target) 
                return sum;
            else {
                if (Math.abs(result - target) > Math.abs(sum - target)) 
                    result = sum;
                if (sum < target)
                    j++;
                else
                    k--;
                }
            }
        }
        return result;
    }
}
