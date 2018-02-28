
nums = [4,5,6,7,0,1,2]

def findMin(nums):
    n = len(nums)
    l = 0
    r = n-1
    while l <= r:
        mid = l+(r-l)/2
        if nums[mid] > nums[n-1]:
            l = mid+1
        else:
            r = mid-1
    return nums[l]

ans = findMin(nums)
print ans
