The algorithm we will implement is a modified form of the very popular Binary Search. Since the rows and columns are pre-sorted, it will be very easy to implement.
​
1. Instead of taking two different calculations to find the middle element, we use only one value of mid and use it to find i and j indices of the middle element.
2. m=len(matrix), n=len(matrix[0])
3. And, low=0, high=(mn)-1
4. Create a while loop with condition low≤high.
5. Calculate mid=(low+high)/2.
6. Take the element to be checked as matrix[mid//n][mid%n]. If the element is the target, we return True.
7. If the element is larger than the target, we move to the left upper section of the matrix by taking high=mid-1. If the element is smaller than the target, we move to the right lower section of the matrix by taking low=mid+1.
8. On coming out of the loop, we return False.
​
Time = O(log(NM)) and Space = O(1)