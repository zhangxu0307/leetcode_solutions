
nums = [12,11,1,6,7]
n = len(nums)
k = 300

tmp = []
for j in xrange(k):
    if j == 0:
        new = nums
    else:
        new = tmp
        tmp = []
    print new
    for i in xrange(n):
        if i != n-1:
            tmp.append((new[i+1]+new[i])%100)
        else:
            tmp.append((new[-1]+new[0])%100)

print new
