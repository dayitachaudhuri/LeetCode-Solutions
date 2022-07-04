class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for item in tokens:
            if item=="+":
                a=stack.pop()
                b=stack.pop()
                stack.append(a+b)
            elif item=="-":
                a=stack.pop()
                b=stack.pop()
                stack.append(b-a)
            elif item=="*":
                a=stack.pop()
                b=stack.pop()
                stack.append(a*b)
            elif item=="/":
                a=stack.pop()
                b=stack.pop() 
                if b%a==0 or b/a>=0:
                    stack.append(b//a)
                else:
                    stack.append(b//a+1)
            else:
                stack.append(int(item))
        
        return stack[0]