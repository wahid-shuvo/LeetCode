def valid_parenthesis(s):
    map = {')': '(', '}': '{', ']': '['}
    stack = []

    for char in s:
        if char in map.keys():
            top_element = stack.pop() if stack else '#'
            if top_element != map[char]:
                return False
        else:
            stack.append(char)

    return not stack


s = ")"
print(valid_parenthesis(s))
