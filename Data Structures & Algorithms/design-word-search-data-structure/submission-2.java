class TrieNode {
    public boolean isTerminal;
    public TrieNode[] next = new TrieNode[26];
}

class WordDictionary {
    private static int CHAR_ALPHABET_BEGIN_INDEX = 97;
    private TrieNode head;

    public WordDictionary() {
        this.head = new TrieNode();
    }

    private int getCharIndexInAlphabet(char c) {
        return c-CHAR_ALPHABET_BEGIN_INDEX;
    }

    public void addWord(String word) {
        var curr = this.head;
        for (char c : word.toCharArray()) {
            var ci = getCharIndexInAlphabet(c);
            var next = curr.next[ci];

            if (next == null) {
                next = new TrieNode();
                curr.next[ci] = next;
            }
            curr = next;
        }
        curr.isTerminal = true;
    }

    private boolean searchFromTrieNode(TrieNode head, String subWord, int startIndex) {
        var curr = head;
        var print = subWord.equals("b..");
        
        for (int i = startIndex; i < subWord.length(); i++) {
            char c = subWord.charAt(i);

            // dot check
            if (c == '.') {
                for (int j = 0; j < curr.next.length; j++) {
                    var subhead = curr.next[j];
                    if (subhead != null && searchFromTrieNode(subhead, subWord, i+1)) {
                        return true;
                    }

                }

                return false;
            }


            var ci = getCharIndexInAlphabet(c);
            var next = curr.next[ci];

            if (next == null) {
                return false;
            }

            curr = next;
        }

        return curr.isTerminal;
    }

    public boolean search(String word) {
        return searchFromTrieNode(this.head, word, 0);
    }
}
