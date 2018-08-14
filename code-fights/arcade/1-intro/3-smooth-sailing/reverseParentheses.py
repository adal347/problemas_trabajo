def doReverse(i, s):
    j = s.find(")")
    reverse = s[i:j]
    s = s[:j] + "" + s[j + 1:]
    s = s[:i] + reverse[::-1] + s[j:]
    return s

def reverseParentheses(s):
    i = s.find("(")
    if i != -1:
        s = s[:i] + "" + s[i + 1:]
        x = s.find("(")
        y = s.find(")")
        if x != -1 and x < y:
            s = reverseParentheses(s)
        elif x != -1 and x > y:
            s = doReverse(i, s)
            s = reverseParentheses(s)
            return s
        s = doReverse(i, s)
    return s
