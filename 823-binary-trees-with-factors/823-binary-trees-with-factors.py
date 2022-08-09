class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        arr.sort()
        children = {num: [] for num in arr}
        trees = {num: 1 for num in arr}
        MOD = 10 ** 9 + 7
        
        for i in range(len(arr) - 1):
            for j in range(i, len(arr) - 1):
                product = arr[i] * arr[j]
                if product in children:
                    children[product].append((arr[i], arr[j]))
                elif product > arr[-1]:
                    break
        
        res = 0
        for num in arr:
            for pair in children[num]:
                trees[num] += (trees[pair[0]] * trees[pair[1]]
                               if pair[0] == pair[1]
                               else 2 * (trees[pair[0]] * trees[pair[1]]))
            trees[num] %= MOD
            res = (res + trees[num]) % MOD
        
        return res