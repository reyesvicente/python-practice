# ============================================================================
# PROBLEM 36: Majority Element
# ============================================================================
# Write a function that finds the majority element in a list.
# The majority element is the element that appears more than n/2 times.
# Assume a majority element always exists.
# Example: majority_element([3, 2, 3]) should return 3
# Example: majority_element([2, 2, 1, 1, 1, 2, 2]) should return 2

def majority_element(lst):
    # Pseudo Code (Boyer-Moore Voting Algorithm):
    # 1. Initialize a candidate variable to None and a counter to 0.
    # 2. Iterate through each element in the list:
    #    a. If the counter is 0, pick the current element as the new candidate.
    #    b. If the current element matches the candidate, increment the counter.
    #    c. If the current element does not match, decrement the counter.
    # 3. Return the candidate (since a majority element always exists).
    candidate = None
    count = 0

    for num in lst:
        if count == 0:
            candidate = num
            count = 1
        elif num == candidate:
            count += 1
        else:
            count -= 1

    return candidate

print(majority_element([3, 2, 3]) )
print(majority_element([2, 2, 1, 1, 1, 2, 2]))


"""
These lines are just standard comments acting as a header to identify the problem number and title.

python
# Write a function that finds the majority element in a list.
# The majority element is the element that appears more than n/2 times.
# Assume a majority element always exists.
This defines the problem. Key takeaways:

A majority element appears more than half the time (e.g., in a list of 10 items, it appears at least 6 times).
We can assume valid input (a solution is guaranteed).
Function Definition
python
def majority_element(lst):
Defines a function named
majority_element
 that takes a single list lst as input.

python
# Pseudo Code (Boyer-Moore Voting Algorithm):
    # 1. Initialize a candidate variable to None and a counter to 0.
    # ...
These are comment lines explaining the plan used below. This specific pattern is called the Boyer-Moore Voting Algorithm.

The Algorithm (Initialization)
python
candidate = None
    count = 0
candidate: Holds the number we currently guess is the majority element. We start with None because we haven't seen any numbers yet.
count: Tracks the "strength" of our current candidate.
The Loop (Voting Process)
python
for num in lst:
Loops through every number (num) in the input list lst, one by one.

The Logic (Inside the Loop)
The logic inside checks three conditions for every number:

1. Is our current streak broken? (Reset)

python
if count == 0:
            candidate = num
            count = 1
If count is 0, it means our previous candidate was completely "cancelled out" by other numbers (or we are just starting).
So, we pick the current number (num) as the new candidate.
We set count to 1 to start its new streak.
2. Is this the same number as our candidate? (Vote Up)

python
elif num == candidate:
            count += 1
If the current num matches our candidate, it gets a "vote."
We increase count to make the candidate stronger.
3. Is this a different number? (Vote Down)

python
else:
            count -= 1
If num is different from the candidate, it "cancels out" one vote for the candidate.
We decrease count.
The Result
python
return candidate
After looping through the entire list, the algorithm mathematically guarantees that if a majority element exists (appears > 50% of the time), it will be the one left in candidate.

Testing
python
print(majority_element([3, 2, 3]) )
Trace:
Processing 3: count is 0 -> candidate becomes 3, count=1.
Processing 2: different from 3 -> count becomes 0.
Processing 3: count is 0 -> candidate becomes 3, count=1.
Result: Returns 3.
python
print(majority_element([2, 2, 1, 1, 1, 2, 2]))
Trace:
Processing 2: candidate=2, count=1.
Processing 2: candidate=2, count=2.
Processing 1: candidate=2, count=1.
Processing 1: candidate=2, count=0.
Processing 1: candidate=1, count=1 (reset!).
Processing 2: candidate=1, count=0.
Processing 2: candidate=2, count=1 (reset!).
Result: Returns 2.
"""