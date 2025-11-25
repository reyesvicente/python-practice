# ============================================================================
# PROBLEM 33: Valid Parentheses
# ============================================================================
# Write a function that checks if a string contains valid matching parentheses.
# Valid pairs: (), [], {}
# Example: is_valid("()") should return True
# Example: is_valid("()[]{}") should return True
# Example: is_valid("(]") should return False
# Example: is_valid("([)]") should return False

def is_valid(s):
    """
    FUNCTION is_valid(s):
        CREATE an empty stack

        CREATE a map of closing to opening brackets:
            pairs = {
                ')': '(',
                ']': '[',
                '}': '{'
            }

        FOR each character c in s:
            IF c is an opening bracket:
                PUSH c onto stack

            ELSE IF c is a closing bracket:
                IF stack is empty:
                    RETURN False

                POP top element from stack → top

                IF top is NOT equal to pairs[c]:
                    RETURN False

        END FOR

        IF stack is empty:
            RETURN True
        ELSE:
            RETURN False
    """
    stack = []
    pairs = {')': '(', ']': '[', '}': '{'}
    for c in s:
        if c in pairs.values():
            stack.append(c)
        elif c in pairs.keys():
            if not stack or stack[-1] != pairs[c]:
                return False
            stack.pop()
    return not stack

print(is_valid("()"))
print(is_valid("()[]{}"))
print(is_valid("(]"))
print(is_valid("([)]"))