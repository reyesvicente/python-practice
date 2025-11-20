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