class TreeNode {
    public boolean isTerminal;
    public Map<Character, TreeNode> next;

    public TreeNode(boolean isTerminal, Map<Character, TreeNode> next) {
        this.isTerminal = isTerminal;
        this.next = next;
    }
}

class PrefixTree {
    private TreeNode head;

    public PrefixTree() {
        this.head = new TreeNode(false, new HashMap<>());
    }

    public void insert(String word) {
        TreeNode curr = this.head;

        for (char c : word.toCharArray()) {
            curr = curr.next.computeIfAbsent(c, k -> new TreeNode(false, new HashMap<>()));
        }
        curr.isTerminal = true;
    }

    private TreeNode findLastNodeInWord(String word) {
        TreeNode curr = this.head;

        for (int i = 0; i < word.length(); i++) {
            var c = word.charAt(i);
            curr = curr.next.get(c);
            
            if (curr == null) {
                return null;
            }
        }

        return curr;
    }

    public boolean search(String word) {
        TreeNode node = this.findLastNodeInWord(word);
        if (node == null) return false;
        return node.isTerminal;
    }

    public boolean startsWith(String prefix) {
        TreeNode node = this.findLastNodeInWord(prefix);
        if (node == null) return false;
        return true;
    }
}
