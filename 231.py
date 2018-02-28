num = 14

def isPowerOfTwo(n):
    two = 1
    while two < n:
        two <<= 1
    if two == n:
        return True
    else:
        return False

ans = isPowerOfTwo(num)
print ans
