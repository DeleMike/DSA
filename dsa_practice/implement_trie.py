class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.isEnd = False

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for ch in word:
            i = ord(ch) - ord("a")
            if curr.children[i] is None:
                curr.children[i] = TrieNode()
            curr = curr.children[i]
        curr.isEnd = True
        
    def search(self, word: str) -> bool:
        curr = self.root
        for ch in word:
            i = ord(ch) - ord("a")
            if curr.children[i] is None:
                return False
            curr = curr.children[i]
        return curr.isEnd
        
    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for ch in prefix:
            i = ord(ch) - ord("a")
            if curr.children[i] == None:
                return False
            curr = curr.children[i]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)