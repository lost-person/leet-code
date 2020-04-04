import java.util.List;
import java.util.Queue;

import javax.swing.tree.TreeNode;

import com.sun.source.tree.Tree;

import java.util.ArrayDeque;
import java.util.LinkedList;

/*
 * @lc app=leetcode id=102 lang=java
 *
 * [102] Binary Tree Level Order Traversal
 *
 * https://leetcode.com/problems/binary-tree-level-order-traversal/description/
 *
 * algorithms
 * Medium (47.04%)
 * Total Accepted:    337.6K
 * Total Submissions: 717.8K
 * Testcase Example:  '[3,9,20,null,null,15,7]'
 *
 * Given a binary tree, return the level order traversal of its nodes' values.
 * (ie, from left to right, level by level).
 * 
 * 
 * For example:
 * Given binary tree [3,9,20,null,null,15,7],
 * 
 * ⁠   3
 * ⁠  / \
 * ⁠ 9  20
 * ⁠   /  \
 * ⁠  15   7
 * 
 * 
 * 
 * return its level order traversal as:
 * 
 * [
 * ⁠ [3],
 * ⁠ [9,20],
 * ⁠ [15,7]
 * ]
 * 
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
    public List<List<Integer>> levelOrder(TreeNode root) {
        // // 方法1 递归
        // List<List<Integer>> list = new LinkedList<>();
        // levelOrderTraversal(root, list, 0);
        // return list;
        // 方法2 队列
        List<List<Integer>> list = new LinkedList<>();
        if(root == null) return list;

        Queue<TreeNode> queue = new ArrayDeque<>();
        queue.offer(root);
        // 某一层的结点
        List<Integer> tmpList;
        TreeNode tmp;
        // 某一层的结点数
        int levelNum = 0;
        int i = 0;
        while(!queue.isEmpty()){
            tmpList = new LinkedList<>();
            levelNum = queue.size();
            // 遍历此层结点
            for(i = 0; i < levelNum; i++){
                tmp = queue.poll();
                tmpList.add(tmp.val);
                if(tmp.left != null) queue.offer(tmp.left);
                if(tmp.right != null) queue.offer(tmp.right);
            }
            list.add(tmpList);
        }
        return list;
    }

    // public void levelOrderTraversal(TreeNode root, List<List<Integer>> list, int level){
    //     if(root != null){
    //         if(level >= list.size()) list.add(new LinkedList<>());
    //         list.get(level).add(root.val);
    //         levelOrderTraversal(root.left, list, level + 1);
    //         levelOrderTraversal(root.right, list, level + 1);
    //     }
    // }
}

