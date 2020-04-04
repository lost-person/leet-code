import java.util.List;
import java.util.Stack;
import java.util.LinkedList;

/*
 * @lc app=leetcode id=144 lang=java
 *
 * [144] Binary Tree Preorder Traversal
 *
 * https://leetcode.com/problems/binary-tree-preorder-traversal/description/
 *
 * algorithms
 * Medium (50.25%)
 * Total Accepted:    306.2K
 * Total Submissions: 609.4K
 * Testcase Example:  '[1,null,2,3]'
 *
 * Given a binary tree, return the preorder traversal of its nodes' values.
 * 
 * Example:
 * 
 * 
 * Input: [1,null,2,3]
 * ⁠  1
 * ⁠   \
 * ⁠    2
 * ⁠   /
 * ⁠  3
 * 
 * Output: [1,2,3]
 * 
 * 
 * Follow up: Recursive solution is trivial, could you do it iteratively?
 * 
 */
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution {
    public List<Integer> preorderTraversal(TreeNode root) {
        // 方法1 递归
        List<Integer> list = new LinkedList<>();
        preOrder(root, list);
        return list;
        // // 方法2 栈
        // List<Integer> list = new LinkedList<>();
        // Stack<TreeNode> stack = new Stack<>();
        // TreeNode t = root;
        // while(t != null || !stack.isEmpty()){
        //     while(t != null){
        //         list.add(t.val);
        //         stack.push(t);
        //         t = t.left;
        //     }
        //     if(!stack.isEmpty()){
        //         t = stack.pop();
        //         t = t.right;
        //     }
        // }
        // return list;
    }

    public void preOrder(TreeNode root, List<Integer> list){
        if(root != null){
            list.add(root.val);
            preOrder(root.left, list);
            preOrder(root.right, list);
        }
    }
}

