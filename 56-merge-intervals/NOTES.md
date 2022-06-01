We initialise a new array with only the first interval. Now we take each interval and try to deduce its correct position in the new array. There can be three cases.
​
1. If the interval's end is before the last interval's end, we do not need to add the interval.
​
2. If the interval starts before the last interval ends and ends after the last interval, we change the end of the last interval to the end of the current interval.
​
3. If the interval starts after the last interval ends, we append the current interval to the new array.