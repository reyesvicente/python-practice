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

"""
    ✅ Line-by-Line Explanation
    Function definition
    def is_valid(s):


    Defines a function is_valid that takes a string s and checks whether its parentheses are valid.

    Create the stack
        stack = []


    Initializes an empty list to use as a stack.
    This stack will store opening brackets as they appear.

    Map closing to opening brackets
        pairs = {')': '(', ']': '[', '}': '{'}


    Creates a dictionary that matches every closing bracket to its corresponding opening bracket.

    Example:
    If you see ) you expect the last opening bracket to be (.

    Iterate through every character in the string
        for c in s:


    Loops through each character c of the input string.

    Check if c is an opening bracket
            if c in pairs.values():
                stack.append(c)


    pairs.values() contains '(', '[', '{'

    If c is one of these, it is an opening bracket

    Push it onto the stack (append)

    Check if c is a closing bracket
            elif c in pairs.keys():


    pairs.keys() contains ')', ']', '}'

    If c is a closing bracket, we must validate it

    Case 1: Stack is empty → invalid
                if not stack or stack[-1] != pairs[c]:
                    return False


    Two invalid scenarios:

    not stack → You found a closing bracket but have nothing to match with
    Example: "]"

    stack[-1] != pairs[c] → The top of the stack does not match
    Example: "([)]"

    Expected ( but found [ before )

    If either case happens → return False.

    If valid, remove the matching opening bracket
                stack.pop()


    Removes the last opening bracket from the stack because it has been correctly matched.

    After the loop finishes
        return not stack


    If the stack is empty, all brackets matched properly → return True

    If the stack still contains opening brackets → return False
    Example: "((("

    not stack is True only when stack is empty.

    ✅ Print results

    These calls test the function:

    print(is_valid("()"))        # True
    print(is_valid("()[]{}"))    # True
    print(is_valid("(]"))        # False
    print(is_valid("([)]"))      # False
"""