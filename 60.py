#encoding=utf-8
n = 9
k = 54494

def getPermutation(n, k):

    visit = [False] * 10
    def dfs(seq,ans):
        import copy
        if len(seq) == n+1:
            tmp = copy.deepcopy(seq[1:])
            ans.append(tmp)
            return
        for i in range(1,n+1):
            if visit[i] == False:
                seq.append(i)
                visit[i] = True
                dfs(seq,ans)
                del seq[-1]
                visit[i] = False
    seq = [0]
    ans = []
    dfs(seq,ans)
    return ''.join(map(str,ans[k-1]))

def getPermutation2(n, k):
    import math
    factor = [math.factorial(i) for i in range(1,n+1)]
    print factor
    visit = [False]*10
    ans = ''
    i = n-2 # factor[n-1]是第n个全排列，factor[n-2]是第n-1个全排列
    k -= 1
    while i >= -1: # i=-1才是最后一个数
        tmp = k/factor[i]
        for j in range(1,n+1):
            if visit[j] == False:
                tmp -= 1
            if tmp < 0:
                break
        visit[j] = True
        ans += str(j)
        k %= factor[i]
        i -= 1
    return ans

def getPermutation3(n, k):
    import math
    factor = [math.factorial(i) for i in range(0, n + 1)] # 0的阶乘也要加入，占位，方便从1-n索引
    print factor
    visit = [False] * (n+1) # n+1个标志位，多一个占位，方便从1-n索引

    ans = ""
    k -= 1

    for i in range(1, n+1): #从1到n遍历
        tmp = k/factor[n-i]
        for j in range(1, n+1): # 从1到n检查有没有用过的数字
            if visit[j] == False:
                if tmp == 0:
                    break
                tmp -= 1
        visit[j] = True
        ans += str(j)
        k %= factor[n-i]
    return ans




ans = getPermutation3(3,5)
print ans


