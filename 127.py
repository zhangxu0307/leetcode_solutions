words = set(["hot","dot","dog","lot","log"])
beginWord = "hit"
endWord = "cog"

b = "kiss"
e = "tusk"
words2 = set(["miss","dusk","kiss","musk","tusk","diss","disk","sang","ties","muss"])

def ladderLength(beginWord, endWord, wordList):

    import string

    n = len(beginWord)
    wordList.add(endWord)

    if beginWord in wordList:
        wordList.remove(beginWord)
    print wordList
    visit = set()
    def dfs(word,length):
        if word == endWord:
            return length
        else:
            for i in range(n):
                for char in string.ascii_lowercase:
                    testWord = word[:i]+char+word[i+1:]
                    if testWord in wordList and testWord != word and testWord not in visit:
                        print testWord
                        visit.add(testWord)
                        ans = dfs(testWord,length+1)
                        visit.remove(testWord)
                        return ans

    if dfs(beginWord,1) == None:
        return 0
    else:
        return dfs(beginWord,1)-1

def ladderLength2(beginWord, endWord, wordList):

    import string
    from collections import deque

    n = len(beginWord)

    def bfs(word,wordList,queue,visit):
        for i in range(n):
            for char in string.ascii_lowercase:
                neighborWord = word[0][:i]+char+word[0][i+1:]
                if neighborWord != word[0] and neighborWord in wordList and neighborWord not in visit:
                    queue.append((neighborWord,word[1]+1))
                    visit.add(neighborWord)
    queue = deque()
    visit = set()
    queue.append((beginWord,1))
    while len(queue) > 0:
        word = queue.popleft()
        if word[0] == endWord:
            return word[1]
        bfs(word,wordList,queue,visit)
    return 0


def ladderLength3(beginWord, endWord, wordList):
    from collections import deque
    letters = list('abcdefghijklmnopqrstuvwxyz')
    def findAllNeighbors(word_dist, wordList, queue, explored):
        for i in range(len(word_dist[0])):
            for l in letters:
                neighbor = word_dist[0][:i] + l + word_dist[0][i + 1:]
                if neighbor != word_dist[0] and neighbor in wordList and neighbor not in explored:
                    queue.append((neighbor, word_dist[1] + 1))
                    explored.add(neighbor)

    word_set = set(wordList)
    queue = deque()
    queue.append((beginWord, 1))
    explored = set()
    while (len(queue) > 0):
        word_dist = queue.popleft()
        if word_dist[0] == endWord:
            return word_dist[1]
        findAllNeighbors(word_dist, word_set, queue, explored)
    return 0

ans = ladderLength(b,e,words2)
print ans
