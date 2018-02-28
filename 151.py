s = "the sky is blue"

def reverseWords(s):

    s = s.strip().split()
    s = s[::-1]
    return ' '.join(s)

ans = reverseWords(s)
print ans
