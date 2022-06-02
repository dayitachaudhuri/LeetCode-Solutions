**Brute Force Solution - **
​
We add all elements of the second array to the first array and then sort the array. Here time complexity will be equal to the complexity of the sorting algorithm (O(N logN)).
​
**Time Optimised Solution - **
​
We can use the two-pointer method to solve the problem in linear time. It is similar to merging two Linked Lists.
​
Use two pointers to point to locations in the two arrays. At each step, check which pointer points to a smaller value, add it to the resultant array and increment it.
Make sure to check if the arrays are empty in the end, if not add their residual values to the resultant array.
​
Time = O(N) and Space = O(N)
This method uses extra space to store the list during traversal.
​
**Space Optimised Solution - **
​
We can solve the problem with no extra space using the swapping method.
Here, the target is to each element from the second array and find its correct position in the first array.
​
* We use a for loop to iterate each element of nums2. Inside the loop, we use a pointer 'a' and a while loop to iterate each element of nums1.
* We compare nums1[a] and nums2[b]. If nums1[a] is greater, we swap the values and increment a.
* When we reach the end of the first array, we put the current value of nums2[b] to the end of nums1.
​
Time = O(N*M) and Space = O(1)
​
**Optimised Solution - **
​
We can further optimise the swapping method to eliminate the need to iterate through each element of the first array and second array in quadratic time. Since the arrays are already sorted, we merely need to partially rearrange the elements.
​
Time = O(logN) and Space = O(1)