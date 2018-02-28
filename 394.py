s = "2[abc]3[cd]ef"
s2 = "3[a2[c]]"
s3 = "3[a]2[bc]"
def decodeString(s):
    from collections import deque
    import string
    sta = deque()
    i,n = 0,len(s)
    while i < n:
        if s[i] in string.digits:
            x = s[i]
            while i+1 < n and s[i+1] in string.digits:
                x += s[i+1]
                i += 1
            sta.append(int(x))
        elif s[i] == '[':
            sta.append(s[i])
        elif s[i] in string.ascii_letters:
            x = s[i]
            while i+1 < n and s[i+1] in string.ascii_letters:
                i += 1
                x += s[i]
            sta.append(x)
        else:
            x = sta.pop()
            while sta[-1] != '[':
                x = sta.pop() + x
            sta.pop()
            repeat = sta.pop()
            sta.append(repeat*x)
        i += 1
    return ''.join(list(sta))


ans = decodeString(s2)
print ans

