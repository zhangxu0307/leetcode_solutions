k = 9
n = 3

def combinationSum3(k, n):

    import copy

    ans = []

    def dfs(sumList, step):
        if step == n and sum(sumList) == k:
            tmp = copy.deepcopy(sumList)
            del tmp[0]
            ans.append(tmp)
        elif step < n:
            for i in range((sumList[-1]+1),10):
                if i >= k:
                    break
                else:
                    sumList.append(i)
                    dfs(sumList, step+1)
                    del sumList[-1]
        else:
            return

    dfs([0],0)
    return ans

ans = combinationSum3(k, n)
print ans


