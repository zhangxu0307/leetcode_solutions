n = 13

def lexicalOrder(n):
    numstr = [str(i) for i in xrange(1,n+1)]
    numstr.sort()
    return list(map(int,numstr))

def lexicalOrder2(n):
    def dfs(num,res):
        if num <= n:
            res.append(num)
            t = num*10
            if t <= n:
                for i in range(10):
                    dfs(t+i,res)

    res = []
    for i in range(1,10):
        dfs(i,res)
    return res


ans = lexicalOrder2(n)
print ans


