class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        par={"[":"]","(":")","{":"}"}
        for i in s:
            if i in par:
                stack.append(i)
            else:
                if len(stack)==0:
                    return False
                if par[stack.pop()]!=i:
                    return False
        if len(stack)==0:
            return True
        return False