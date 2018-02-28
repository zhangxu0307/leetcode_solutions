bad = 1
n = 1

[True]

def firstBadVersion(n):
    low = 1
    high = n+1
    while low < high:
        mid = (low+high)//2
        if isBadVersion(mid):
            high = mid
        else:
            low = mid + 1
    return low

ans = firstBadVersion(n)
print ans


