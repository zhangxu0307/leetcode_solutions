
nums2 = [1,2,2,1,3,4,5]
nums1 = [2,2,5]
def intersect(nums1, nums2):
    hash = {}
    n1 = len(nums1)
    n2 = len(nums2)
    ans = []
    for i in range(n1):
        if nums1[i] in hash:
            hash[nums1[i]] += 1
        else:
            hash[nums1[i]] = 1
    for i in range(n2):
        if nums2[i] in hash:
            if hash[nums2[i]] != 0:
                ans.append(nums2[i])
                hash[nums2[i]] -= 1
    return ans

ans = intersect(nums1,nums2)
print ans