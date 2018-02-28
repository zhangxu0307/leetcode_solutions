nums = [2,0]

def missingNumber(nums):

    n = len(nums)
    nums.sort()
    if nums[n-1] != n:
        return n
    if nums[0] != 0:
        return 0
    for i in range(1,n):
        if nums[i-1]+1 != nums[i]:
            return nums[i-1]+1

def missingNumber2(nums):
    sum1 = sum(nums)
    n = len(nums)
    sum2 = (n*(n+1))/2
    return sum2-sum1


ans = missingNumber2(nums)
print ans