class Solution:
    def romanToInt(self, s: str) -> int:
        rom = {"I" : 1,
          "V" : 5,
          "X" : 10,
          "L" : 50,
          "C" : 100,
          "D" : 500,
          "M" : 1000}
    
        size=len(s)
        current=0
        old=0
        total=0
        i=0
        while  i < size:
            current=rom[s[i]]
            i+=1
            if current<=old:
                total+=old
                old=current
                continue
            old=current-old
        total+=old
        return total