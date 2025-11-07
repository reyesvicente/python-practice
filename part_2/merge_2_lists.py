# ============================================================================
# PROBLEM 16: Merge Two Sorted Lists
# ============================================================================
# Write a function that merges two sorted lists into one sorted list.
# Do NOT use the sort() function or sorted().
# Example: merge_sorted([1, 3, 5], [2, 4, 6]) should return [1, 2, 3, 4, 5, 6]

def merge_sorted(lst1, lst2):
    """
        PSEUDO CODE:
        function merge_sorted(lst1, lst2):
        initialize an empty list merged_list
        initialize two pointers i and j to 0

        while i < length of lst1 and j < length of lst2:
            if element at lst1[i] is less than or equal to element at lst2[j]:
                append lst1[i] to merged_list
                increment i by 1
            else:
                append lst2[j] to merged_list
                increment j by 1

        while i < length of lst1:
            append lst1[i] to merged_list
            increment i by 1

        while j < length of lst2:
            append lst2[j] to merged_list
            increment j by 1

        return merged_list
    """
    merged_list = []
    i = 0
    j = 0

    while i < len(lst1) and j < len(lst2):
        if lst1[i] <= lst2[j]:
            merged_list.append(lst1[i])
            i += 1
        else:
            merged_list.append(lst2[j])
            j += 1

    while i < len(lst1):
        merged_list.append(lst1[i])
        i += 1

    while j < len(lst2):
        merged_list.append(lst2[j])
        j += 1

    return merged_list


print(merge_sorted([1, 3, 5], [2, 4, 6]))

"""
Let me explain how this merge algorithm works step by step:

Initialization:
merged_list: Empty list to store the final sorted result
i: Pointer for lst1 (starts at index 0)
j: pointer for lst2 (starts at index 0)
Main Merging Loop:
python
while i < len(lst1) and j < len(lst2):
This loop runs as long as there are elements remaining in both lists. It compares elements at the current positions of both lists and appends the smaller one to merged_list.
Element Comparison:
python
if lst1[i] <= lst2[j]:
    merged_list.append(lst1[i])
    i += 1
else:
    merged_list.append(lst2[j])
    j += 1
If the current element in lst1 is less than or equal to the current element in lst2, take from lst1 and move its pointer forward
Otherwise, take from lst2 and move its pointer forward
Handle Remaining Elements:
python
while i < len(lst1):
    merged_list.append(lst1[i])
    i += 1

while j < len(lst2):
    merged_list.append(lst2[j])
    j += 1
These loops handle any remaining elements in either list after one list is exhausted. Since the input lists are already sorted, we can simply append the remaining elements to the result.
Return Result:
python
return merged_list
Returns the final merged and sorted list.
Example with [1, 3, 5] and [2, 4, 6]:

Compare 1 and 2 → take 1
Compare 3 and 2 → take 2
Compare 3 and 4 → take 3
Compare 5 and 4 → take 4
Compare 5 and 6 → take 5
First list is exhausted, append remaining [6] from second list
Final result: [1, 2, 3, 4, 5, 6]
The time complexity is O(n + m) where n and m are the lengths of the two lists, as each element is processed exactly once.
"""