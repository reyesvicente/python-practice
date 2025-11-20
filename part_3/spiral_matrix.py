# ============================================================================
# PROBLEM 29: Spiral Matrix
# ============================================================================
# Write a function that returns the elements of a 2D matrix in spiral order (clockwise).
# Start from the top-left and spiral inward.
# Example: spiral_matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) should return [1, 2, 3, 6, 9, 8, 7, 4, 5]

def spiral_matrix(matrix):
    """
        PSEUDO CODE:
        FUNCTION spiral_matrix(matrix):
            # 1. Handle Edge Case
            IF matrix is empty OR matrix has no columns:
                RETURN empty list

            # 2. Initialize Variables
            result = empty list
            top = 0
            bottom = number of rows in matrix - 1
            left = 0
            right = number of columns in matrix - 1

            # 3. Loop until boundaries meet or cross
            WHILE top <= bottom AND left <= right:

                # Traverse from Left to Right along the Top row
                FOR column FROM left TO right:
                    APPEND matrix[top][column] TO result
                INCREMENT top  # Top row is done

                # Traverse from Top to Bottom along the Right column
                FOR row FROM top TO bottom:
                    APPEND matrix[row][right] TO result
                DECREMENT right  # Right column is done

                # Check if there are still rows remaining
                IF top <= bottom:
                    # Traverse from Right to Left along the Bottom row
                    FOR column FROM right DOWN TO left:
                        APPEND matrix[bottom][column] TO result
                    DECREMENT bottom  # Bottom row is done

                # Check if there are still columns remaining
                IF left <= right:
                    # Traverse from Bottom to Top along the Left column
                    FOR row FROM bottom DOWN TO top:
                        APPEND matrix[row][left] TO result
                    INCREMENT left  # Left column is done

            # 4. Return the collected elements
            RETURN result
    """
    if matrix is None or matrix == []:
        return []

    result = []
    top = 0
    bottom = len(matrix) - 1
    left = 0
    right = len(matrix[0]) - 1

    while top <= bottom and left <= right:
        for i in range(left, right + 1):
            result.append(matrix[top][i])
        top += 1

        for i in range(top, bottom + 1):
            result.append(matrix[i][right])
        right -= 1

        if top <= bottom:
            for i in range(right, left - 1, -1):
                result.append(matrix[bottom][i])
            bottom -= 1

        if left <= right:
            for i in range(bottom, top - 1, -1):
                result.append(matrix[i][left])
            left += 1

    return result

print(spiral_matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))

"""
    Here is a line-by-line explanation of the
    spiral_matrix
    function:

    1. Edge Case Handling
    python
    if matrix is None or matrix == []:
        return []
    Check: It first checks if the input
    matrix
    is None or an empty list [].
    Action: If either is true, it immediately returns an empty list [] because there are no elements to traverse.
    2. Initialization
    python
    result = []
    top = 0
    bottom = len(matrix) - 1
    left = 0
    right = len(matrix[0]) - 1
    result = []: Creates an empty list to store the numbers as we find them.
    top = 0: Sets the boundary for the top row (starts at index 0).
    bottom = len(matrix) - 1: Sets the boundary for the bottom row (last index of rows).
    left = 0: Sets the boundary for the left column (starts at index 0).
    right = len(matrix[0]) - 1: Sets the boundary for the right column (last index of columns).
    3. The Main Loop
    python
    while top <= bottom and left <= right:
    Condition: The loop continues as long as the boundaries haven't crossed each other. If top exceeds bottom or left exceeds right, it means we have finished traversing the entire matrix.
    4. Traverse Top Row (Left → Right)
    python
        for i in range(left, right + 1):
            result.append(matrix[top][i])
        top += 1
    Loop: Iterates through columns from left to right.
    Append: Adds the elements of the current top row to result.
    Update: top += 1 moves the top boundary down by one, effectively "removing" the row we just processed.
    5. Traverse Right Column (Top → Bottom)
    python
        for i in range(top, bottom + 1):
            result.append(matrix[i][right])
        right -= 1
    Loop: Iterates through rows from the new top to bottom.
    Append: Adds the elements of the current right column to result.
    Update: right -= 1 moves the right boundary left by one, "removing" the column we just processed.
    6. Traverse Bottom Row (Right → Left)
    python
        if top <= bottom:
            for i in range(right, left - 1, -1):
                result.append(matrix[bottom][i])
            bottom -= 1
    Check (if top <= bottom): This is crucial! Since we moved top down earlier, we must ensure we haven't already finished the rows. This prevents processing the same row twice in a single-row matrix.
    Loop: Iterates backwards from right down to left.
    Append: Adds elements of the bottom row to result.
    Update: bottom -= 1 moves the bottom boundary up.
    7. Traverse Left Column (Bottom → Top)
    python
        if left <= right:
            for i in range(bottom, top - 1, -1):
                result.append(matrix[i][left])
            left += 1
    Check (if left <= right): Similar to the previous check, this ensures we don't re-process a column if the right boundary has moved past left.
    Loop: Iterates backwards from bottom up to top.
    Append: Adds elements of the left column to result.
    Update: left += 1 moves the left boundary to the right.
    8. Return Result
    python
    return result
    Once the while loop finishes (boundaries have crossed), the function returns the final result list containing the spiral order.
"""