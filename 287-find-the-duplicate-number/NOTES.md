**Brute Force - **
​
Sort the array. Find out which consecutive values are equal.
​
**Using Extra Space - **
​
Use a list to store the number of occurrences of each value. Use it to find the value that occurred twice.
​
**Optimised Solution - **
​
We can use the two-pointer method to solve this problem as well.
​
1. We will initialise a slow pointer and a fast pointer.
2. We enter into a loop. At each step, we increment the slow pointer as nums[slow] and the fast pointer as nums[nums[fast]]. When both pointers have the same value, we break the loop.
3. We reinitialise fast as 0 and enter another loop. This time we increment the slow pointer as nums[slow] and the fast pointer as nums[fast]. When both pointers have the same value, this value is the duplicated value.