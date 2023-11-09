class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:


        stack = [asteroids[0]]
        for index in range(1,len(asteroids)):

            num = asteroids[index]
            to_be_added =True
            while(stack and ((num<0 and stack[-1]>0))):
                if(abs(num)==abs(stack[-1])):
                    stack.pop()
                    to_be_added=False
                    break
                elif(abs(num)<abs(stack[-1])):
                    to_be_added=False
                    break
                else:
                    stack.pop()
            
            if to_be_added:
                stack.append(num)

        return stack