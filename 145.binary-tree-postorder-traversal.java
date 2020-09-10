import java.util.List;
import java.util.Stack;

import javax.swing.tree.TreeNode;

import java.util.LinkedList;

/*
 * @lc app=leetcode id=145 lang=java
 *
 * [145] Binary Tree Postorder Traversal
 *
 * https://leetcode.com/problems/binary-tree-postorder-traversal/description/
 *
 * algorithms
 * Hard (46.89%)
 * Total Accepted:    236.6K
 * Total Submissions: 504.7K
 * Testcase Example:  '[1,null,2,3]'
 *
 * Given a binary tree, return the postorder traversal of its nodes' values.
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
 * Output: [3,2,1]
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
    public List<Integer> postorderTraversal(TreeNode root) {
        // // 方法1 递归
        // List<Integer> list = new LinkedList<>();
        // postOrder(root, list);
        // return list;
        // 方法2 栈
        List<Integer> list = new LinkedList<>();
        if(root == null) return list;
        Stack<TreeNode> stack = new Stack<>();
        stack.push(root);
        TreeNode cur = null, pre = null;
        while(!stack.isEmpty()){
            cur = stack.peek();
            // 左右孩子为空，或者左右孩子已经遍历
            if((cur.left == null && cur.right == null) || 
                (pre != null && (pre == cur.left || pre == cur.right))){
                list.add(cur.val);
                stack.pop();
                pre = cur;
            }
            else{
                // 先压右孩子
                if(cur.right != null) stack.push(cur.right);
                if(cur.left != null) stack.push(cur.left);
            }
        }
        return list;
    }

    public void postOrder(TreeNode root, List<Integer> list){
        if(root != null){
            postOrder(root.left, list);
            postOrder(root.right, list);
            list.add(root.val);
        }
    }
}

