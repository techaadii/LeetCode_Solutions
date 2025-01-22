#Solution to LeetCode Problem 412-FIZZ BUZZ

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        arr=[]
        string=""
        
        for i in range(1,n+1):
            if i%3==0 and i%5==0:
                string="FizzBuzz"
                arr.append(string)
            
            elif i%3==0:
                string="Fizz"
                arr.append(string)
            

            elif i%5==0:
                string="Buzz"
                arr.append(string)
            else:
                arr.append(str(i))

        return arr
        