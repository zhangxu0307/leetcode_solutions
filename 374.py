n = 10
target = 6
def guess(num):
    if num > target:
        return 1
    elif num < target:
        return -1
    else:
        return 0



def guessNumber(n):
    l = 1
    r = n
    while l < r:
        mid = l + (r - l) / 2
        if guess(mid) == 1:
            r = mid-1
        elif guess(mid) == -1:
            l = mid+1
        else:
            return mid
ans = guessNumber(n)
print ans

