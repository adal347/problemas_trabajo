def reverseInParentheses(s):
    return eval('"' + s.replace('(', '"+("').replace(')', '")[::-1]+"') + '"')