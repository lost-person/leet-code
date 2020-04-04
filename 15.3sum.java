import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/*
 * @lc app=leetcode id=15 lang=java
 *
 * [15] 3Sum
 *
 * https://leetcode.com/problems/3sum/description/
 *
 * algorithms
 * Medium (23.27%)
 * Total Accepted:    477.6K
 * Total Submissions: 2.1M
 * Testcase Example:  '[-1,0,1,2,-1,-4]'
 *
 * Given an array nums of n integers, are there elements a, b, c in nums such
 * that a + b + c = 0? Find all unique triplets in the array which gives the
 * sum of zero.
 * 
 * Note:
 * 
 * The solution set must not contain duplicate triplets.
 * 
 * Example:
 * 
 * 
 * Given array nums = [-1, 0, 1, 2, -1, -4],
 * 
 * A solution set is:
 * [
 * ⁠ [-1, 0, 1],
 * ⁠ [-1, -1, 2]
 * ]
 * 
 * 
 */
class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        // 方法1 有点low
        // 记录结果
        List<List<Integer>> list = new ArrayList<>();

        /**
         *  map HashMap
         *      key Integer nums中的元素; value Integer 下标
         *  */
        Map<Integer, Integer> map = new HashMap<>();

        Arrays.sort(nums);
        int n = nums.length;

        int i = 0, j = 0;
        for(; i < n; i++)
            map.put(nums[i], i);
        
        int target = 0;
        Integer index = 0;
        for(i = 0; i < n - 2; i++){
            // 避免重复
            if(i > 0 && nums[i] == nums[i - 1]) continue;
            for(j = i + 1; j < n - 1; j++){
                if(j > i + 1 && nums[j] == nums[j - 1]) continue;
                target = 0 - nums[i] - nums[j];
                index = map.get(target);
                if(index != null && index > j)
                    list.add(Arrays.asList(nums[i], nums[j], target));
            }
        }
        return list;
        // 方法2
    }

	public List<List<Integer>> kSum(int[] A, int start, int end, int target, int k)
	{
		List<List<Integer>> list = new ArrayList<>();
		
		if(k == 2)
		{
			while(start < end)
			{
				if(A[start] + A[end] == target)
				{
					list.add(new LinkedList<Integer>(Arrays.asList(A[start], target - A[start])));
					while(start < end && A[start] == A[start + 1]) start++;
					while(start < end && A[end] == A[end - 1]) end--;
					start++;
					end--;
				}
				else if (A[start] + A[end] < target)
					start++;
				else
					end--;				
			}
		}
		else // Reduce kSum to (k - 1)sum
		{
			for(int i = start; i < A.length - k + 1 && A[i] * k <= target; i++)
			{
				if(i == start || A[i] != A[i - 1])
				{
					List<List<Integer>> mainList = kSum(A, i + 1, A.length - 1, target - A[i], k - 1);					
					for(List<Integer> subList : mainList)
						subList.add(0, A[i]);
					list.addAll(mainList);
				}
			}	
		}
		return list;
	}
}
