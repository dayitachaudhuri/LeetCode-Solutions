class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        '''2 4 8 16 32 64 128 256'''
        return sorted(str(n)) in [sorted(str(1 << i)) for i in range(30)] 