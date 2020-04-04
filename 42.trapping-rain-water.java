/*
 * @lc app=leetcode id=42 lang=java
 *
 * [42] Trapping Rain Water
 *
 * https://leetcode.com/problems/trapping-rain-water/description/
 *
 * algorithms
 * Hard (41.82%)
 * Total Accepted:    256K
 * Total Submissions: 612.1K
 * Testcase Example:  '[0,1,0,2,1,0,1,3,2,1,2,1]'
 *
 * Given n non-negative integers representing an elevation map where the width
 * of each bar is 1, compute how much water it is able to trap after raining.
 * 
 * 
 * The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1].
 * In this case, 6 units of rain water (blue section) are being trapped. Thanks
 * Marcos for contributing this image!
 * 
 * Example:
 * 
 * 
 * Input: [0,1,0,2,1,0,1,3,2,1,2,1]
 * Output: 6
 * 
 */
class Solution {
    public int trap(int[] height) {
        int h = 0;
        int area = 0;
        int i = 0, j = height.length - 1;
        while(i < j){
            if(height[i] < height[j]){
                h = Math.max(h, height[i]);
                area += h - height[i];
                i++;
            }
            else{
                h = Math.max(h, height[j]);
                area += h - height[j];
                j--;
            }
        }
        return area;
    }
}

