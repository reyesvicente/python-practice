# ============================================================================
# PROBLEM 15: Remove Outliers
# ============================================================================
# Write a function that removes numbers that are significantly different from the rest.
# Remove any number that is more than 2 standard deviations away from the mean.
# Hint: You may need to calculate mean and standard deviation.
# Example: remove_outliers([1, 2, 3, 4, 5, 100]) should return [1, 2, 3, 4, 5]

def remove_outliers(lst):
    """
        function remove_outliers(list):
        calculate the mean of the list
        calculate the standard deviation of the list

        create an empty list to store filtered values

        for each number in the list:
            if the number is within 2 standard deviations from the mean:
                add the number to the filtered list

        return the filtered list
    """
    if not lst:
        return []
    mean_of_list = sum(lst) / len(lst)
    variance = sum((x - mean_of_list) ** 2 for x in lst) / len(lst)
    std_dev = variance ** 0.5
    lower_bound = mean_of_list - 2 * std_dev
    upper_bound = mean_of_list + 2 * std_dev
    return [x for x in lst if lower_bound <= x <= upper_bound]

print(remove_outliers([1, 2, 3, 4, 5, 100]))

"""
Let me break down the code for you:

python
def remove_outliers(lst):
    # Handle empty list case
    if not lst:
        return []

    # Calculate the mean (average) of the list
    mean_of_list = sum(lst) / len(lst)

    # Calculate variance: average of squared differences from the mean
    variance = sum((x - mean_of_list) ** 2 for x in lst) / len(lst)

    # Standard deviation is the square root of variance
    std_dev = variance ** 0.5

    # Define bounds for values within 2 standard deviations from the mean
    lower_bound = mean_of_list - 2 * std_dev
    upper_bound = mean_of_list + 2 * std_dev

    # Return only values within these bounds
    return [x for x in lst if lower_bound <= x <= upper_bound]

# Test the function
print(remove_outliers([1, 2, 3, 4, 5, 100]))  # Output: [1, 2, 3, 4, 5]
Key Points:
Mean Calculation: Computes the average of all numbers in the list.
Variance Calculation: Measures how far each number in the list is from the mean, then squares those differences and averages them.
Standard Deviation: The square root of variance, indicating how spread out the numbers are.
Bounds: Any number more than 2 standard deviations away from the mean is considered an outlier.
List Comprehension: Filters out numbers outside the bounds.
For the input [1, 2, 3, 4, 5, 100], the mean is about 19.17, and the standard deviation is about 38.74. The bounds are approximately -58.31 to 96.65. Since 100 is outside this range, it's removed, leaving [1, 2, 3, 4, 5].
"""
