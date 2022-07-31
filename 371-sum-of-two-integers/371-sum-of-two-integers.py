class Solution:
    def getSum(self, a: int, b: int) -> int:
        
        positive=[]
        negative=[]
        
        if a>0:
            for i in range(a):
                positive.append(1)
        else:
            for i in range(-1*a):
                negative.append(1)
                
        if b>0:
            for j in range(b):
                positive.append(1)
        else:
            for j in range(-1*b):
                negative.append(1)
                
        if len(positive)==len(negative):
            return 0
        elif len(positive)>len(negative):
            for k in range(len(negative)):
                positive.pop()
            return len(positive)
        else:
            for i in range(len(positive)):
                negative.pop()
            return -1*len(negative)