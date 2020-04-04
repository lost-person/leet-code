/*
 * @lc app=leetcode id=4 lang=java
 *
 * [4] Median of Two Sorted Arrays
 *
 * https://leetcode.com/problems/median-of-two-sorted-arrays/description/
 *
 * algorithms
 * Hard (25.39%)
 * Total Accepted:    378.4K
 * Total Submissions: 1.5M
 * Testcase Example:  '[1,3]\n[2]'
 *
 * There are two sorted arrays nums1 and nums2 of size m and n respectively.
 * 
 * Find the median of the two sorted arrays. The overall run time complexity
 * should be O(log (m+n)).
 * 
 * You may assume nums1 and nums2 cannot be both empty.
 * 
 * Example 1:
 * 
 * 
 * nums1 = [1, 3]
 * nums2 = [2]
 * 
 * The median is 2.0
 * 
 * 
 * Example 2:
 * 
 * 
 * nums1 = [1, 2]
 * nums2 = [3, 4]
 * 
 * The median is (2 + 3)/2 = 2.5
 * 
 * 
 */
class Solution {
    // 分治法，二分查找（没想到，要二刷）
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        if(nums1.length >= nums2.length){
            int []temp = nums1;
            nums1 = nums2;
            nums2 = temp;
        }
        int m = nums1.length;
        int n = nums2.length;
        // i在[0, m]中寻找
        int iMin = 0, iMax = m;
        // 中位数下标
        int mid = (m + n + 1) / 2;
        int i = 0, j = 0;
        while(iMin <= iMax){
            i = (iMin + iMax) / 2;
            j = mid - i;
            // 下标为i的数太小，增加
            if(i < iMax && nums2[j - 1] > nums1[i])
                iMin = i + 1;
            // 下标为i的数太大，减少
            else if(i > iMin && nums1[i - 1] > nums2[j])
                iMax = i - 1;
            // 下标为i的数正好
            else{
                int maxLeft = 0;
                if(i == 0) maxLeft = nums2[j - 1];
                else if(j == 0) maxLeft = nums1[i - 1];
                else
                    maxLeft = Math.max(nums1[i - 1], nums2[j - 1]);
                if((m + n) % 2 == 1) return maxLeft;
                int minRight = 0;
                if(i == m) minRight = nums2[j];
                else if(j == n) minRight = nums1[i];
                else
                    minRight = Math.min(nums1[i], nums2[j]);
                return (maxLeft + minRight) / 2.0;
            }
        }
        return 0.0;
    }
}
