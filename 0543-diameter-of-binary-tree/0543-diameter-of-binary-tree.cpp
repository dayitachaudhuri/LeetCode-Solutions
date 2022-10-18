/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    int dia=0;
    int dfs(TreeNode* root){
            if (!root)
                return 0;
            int left = dfs(root->left);
            int right = dfs(root->right);
            if (left+right > dia)
                dia = left + right;
            if (left > right)
                return 1 + left;
            return 1 + right;
        }
    int diameterOfBinaryTree(TreeNode* root) {       
        dfs(root);
        return dia;
    }
};