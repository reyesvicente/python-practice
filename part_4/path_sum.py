# ============================================================================
# PROBLEM 39: Path Sum
# ============================================================================
# Write a function that checks if a binary tree has a root-to-leaf path with a given sum.
# A path must go from root to a leaf (node with no children).
# Example: For a tree with root-to-leaf paths summing to 22, path_sum(root, 22) should return True

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def path_sum(root, target_sum):
    # PSEUDOCODE:
    # If root is None:
    #     Return False
    if not root:
        return False

    # Check if the current node is a leaf (has no children)
    # If root.left is None AND root.right is None:
    #     Return True if target_sum equals root.val
    #     Else Return False
    if not root.left and not root.right:
        return root.val == target_sum

    # Recursive step:
    # Calculate the remaining sum needed: new_target = target_sum - root.val
    new_target = target_sum - root.val

    # Check left subtree: result_left = path_sum(root.left, new_target)
    # Check right subtree: result_right = path_sum(root.right, new_target)

    # Return True if either result_left OR result_right is True
    return path_sum(root.left, new_target) or path_sum(root.right, new_target)

if __name__ == "__main__":
    # Example tree:
    #       5
    #      / \
    #     4   8
    #    /   / \
    #   11  13  4
    #  /  \      \
    # 7    2      1

    root = TreeNode(5)
    root.left = TreeNode(4)
    root.right = TreeNode(8)
    root.left.left = TreeNode(11)
    root.left.left.left = TreeNode(7)
    root.left.left.right = TreeNode(2)
    root.right.left = TreeNode(13)
    root.right.right = TreeNode(4)
    root.right.right.right = TreeNode(1)

    # Test cases
    print(f"path_sum(root, 22) => {path_sum(root, 22)}") # Expected: True (5 -> 4 -> 11 -> 2)
    print(f"path_sum(root, 26) => {path_sum(root, 26)}") # Expected: True (5 -> 8 -> 13)
    print(f"path_sum(root, 18) => {path_sum(root, 18)}") # Expected: True (5 -> 8 -> 4 -> 1)
    print(f"path_sum(root, 100) => {path_sum(root, 100)}") # Expected: False


"""
Explanation of the Code:

1. TreeNode Class
   - This class defines the structure of a node in a binary tree.
   - Each node has a value (`val`) and pointers to left and right children (`left`, `right`).

2. path_sum Function
   - Purpose: Check if there exists a path from the root to a leaf such that the sum of values along the path equals `target_sum`.
   - Logic:
     - Base Case 1: If `root` is `None` (empty tree or reached past a leaf), return `False`. An empty path cannot have a sum.
     - Base Case 2: If the current node is a leaf (no left or right children), check if its value matches the `target_sum`. If yes, we found a valid path!
     - Recursive Step: If it's not a leaf, we need to continue checking down the tree.
       - We subtract the current node's value from `target_sum` (`new_target = target_sum - root.val`).
       - We recursively call `path_sum` on the left child AND the right child with the `new_target`.
       - If EITHER the left path OR the right path returns `True`, then a valid path exists.

3. Execution Block (if __name__ == "__main__":)
   - Creates a sample binary tree manually to test the function.
   - Runs `path_sum` with various target sums to verify correctness.
   - Prints the results to the console.

Trace Example (path_sum(root, 22)):
   - Start at 5. Target: 22. New Target: 17.
   - Go Left to 4. Target: 17. New Target: 13.
   - Go Left to 11. Target: 13. New Target: 2.
   - Go Right to 2. Target: 2. New Target: 0.
   - Node 2 is a leaf. 2 == 2 is True. Return True.
   - Property propagates up: True -> True -> True.
"""

"""
Claude AI pseudo code:
FUNCTION path_sum(root, target_sum):
    // Base case: empty tree has no paths
    IF root is NULL:
        RETURN False

    // Check if we're at a leaf node
    IF root.left is NULL AND root.right is NULL:
        // At leaf: check if current value equals remaining sum
        RETURN root.value == target_sum

    // Recursive case: check left and right subtrees
    // Subtract current node's value from target_sum
    remaining_sum = target_sum - root.value

    // Check if either left or right subtree has a valid path
    left_has_path = path_sum(root.left, remaining_sum)
    right_has_path = path_sum(root.right, remaining_sum)

    // Return True if either subtree has a valid path
    RETURN left_has_path OR right_has_path


// Alternative iterative approach using stack:
FUNCTION path_sum_iterative(root, target_sum):
    IF root is NULL:
        RETURN False

    // Stack stores pairs of (node, remaining_sum)
    stack = [(root, target_sum)]

    WHILE stack is not empty:
        (current_node, remaining) = stack.pop()

        // Check if leaf node with matching sum
        IF current_node.left is NULL AND current_node.right is NULL:
            IF current_node.value == remaining:
                RETURN True

        // Add children to stack with updated remaining sum
        new_remaining = remaining - current_node.value

        IF current_node.right is not NULL:
            stack.push((current_node.right, new_remaining))

        IF current_node.left is not NULL:
            stack.push((current_node.left, new_remaining))

    RETURN False
"""