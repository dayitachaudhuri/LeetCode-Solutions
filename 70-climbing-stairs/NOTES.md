Recursion -
1. if n<=2: return n
2. return recurse(n-2)+recurse(n-1)
​
DP -
1. Outside function cache={1:1,2:2}
2. if n in cache: return cache[n]
3. value=recurse(n-2)+recurse(n-1), cache[n]=value, return value"