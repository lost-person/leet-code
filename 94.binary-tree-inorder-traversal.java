import java.util.LinkedList;
import java.util.List;
import java.util.Stack;

/*
 * @lc app=leetcode id=94 lang=java
 *
 * [94] Binary Tree Inorder Traversal
 *
 * https://leetcode.com/problems/binary-tree-inorder-traversal/description/
 *
 * algorithms
 * Medium (55.05%)
 * Total Accepted:    411K
 * Total Submissions: 746.7K
 * Testcase Example:  '[1,null,2,3]'
 *
 * Given a binary tree, return the inorder traversal of its nodes' values.
 * 
 * Example:
 * 
 * 
 * Input: [1,null,2,3]
 * ⁠  1
 * ⁠   \
 * ⁠    2
 * ⁠   /
 * ⁠  3
 * 
 * Output: [1,3,2]
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
    public List<Integer> inorderTraversal(TreeNode root) {
        // 方法1 递归
        List<Integer> list = new LinkedList<>();
        inOrder(root, list);
        return list;
        // // 方法2 栈
        // Stack<TreeNode> stack = new Stack<>();
        // TreeNode t = root;
        // while(t != null || !stack.isEmpty()){
        //     // 不断压入左孩子
        //     if(t != null){
        //         stack.push(t);
        //         t = t.left;
        //     }
        //     // 没有左孩子，出栈
        //     else{
        //         t = stack.pop();
        //         list.add(t.val);
        //         t = t.right;
        //     }
        // }
        // return list;
    }

    public void inOrder(TreeNode root, List<Integer> list){
        if(root != null){
            inOrder(root.left, list);
            list.add(root.val);
            inOrder(root.right, list);
        }
    }
}

