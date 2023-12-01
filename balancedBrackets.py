def isBalanced(string):
    stack = []
    open_brackets = set(["[", "{", "("])
    bracket_pairs = {"]": "[", "}": "{", ")": "("}

    for bracket in string:
        if bracket in open_brackets:
            stack.append(bracket)
        elif bracket in bracket_pairs:
            if not stack or stack.pop() != bracket_pairs[bracket]:
                return "NO"
    return "YES" if not stack else "NO"
#main
n = int(input().strip())
for i in range(n):
    string = input().strip()
    result = isBalanced(string)
    print(result)