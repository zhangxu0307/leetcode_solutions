s = ["abcw", "baz", "foo", "bar", "xtfn", "abcdef"]

def maxProduct(words):
    nums = []
    n = len(words)
    maxlen = 0
    for word in words:
        nums.append(sum(1<<(ord(char)-ord('a')) for char in set(word)))
    print nums
    for i in range(n):
        for j in range(n):
            if not (nums[i] & nums[j]):
                maxlen = max(len(words[i])*len(words[j]),maxlen)
    return maxlen

ans = maxProduct(s)
print ans
