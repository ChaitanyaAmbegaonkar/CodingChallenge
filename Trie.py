class TrieNode:

    def __init__(self):
        self.children = [None] * 26
        self.isEndOfWord = False

class Trie:

    def __init__(self):
        self.root = self.getNode()

    def getNode(self):
        return TrieNode()

    def _charToIndex(self, ch):
        return ord(ch) - ord('a')

    def buildTrie(self,words):
        root = self.root
        for j in words:

            i = self._charToIndex(j)
            if not root.children[i]:
                root.children[i] = self.getNode()
            root = root.children[i]
        root.isEndOfWord = True

    def search(self,word):
        print word
        root = self.root
        for j in word:
            i = self._charToIndex(j)
            if not root.children[i]:
                print "Not Found"
                return
            root = root.children[i]

        if root.isEndOfWord:
            print "Found"
            return
        else:
            print "Not Found"
            return

    def dfs(self,root):
        for i in range(26):
            if root.children[i]:
                print i
                self.dfs(root.children[i])



def main():
    words = ['his', 'hers', 'her', 'she']
    t = Trie()
    for i in words:
        t.buildTrie(i)

    t.dfs(t.root)
    t.search('he')

if __name__ == '__main__':
    main()
