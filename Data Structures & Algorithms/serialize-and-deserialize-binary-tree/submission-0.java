/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

public class Codec {
    int i = 0;

    // Encodes a tree to a single string.
    public String serialize(TreeNode root) {
        if (root == null) return "-";
        
        StringBuilder builder = new StringBuilder(String.valueOf(root.val));

        return builder
            .append("|")
            .append(serialize(root.left))
            .append("|")
            .append(serialize(root.right))
            .toString();
    }

    // Decodes your encoded data to tree.
    public TreeNode deserialize(String data) {
        int numberEnd = data.indexOf('|', i);
        String value;

        if (numberEnd == -1) value = data.substring(i);
        else {
            value = data.substring(i, numberEnd);
            i = numberEnd + 1;
        }

        if (value.equals("-")) return null;

        int number = Integer.parseInt(value);
        

        TreeNode root = new TreeNode(number);
        root.left = deserialize(data);
        root.right = deserialize(data);
        return root;
    }
}
