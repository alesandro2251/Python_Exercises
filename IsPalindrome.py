class Solution:
    def isPalindrome(self, x: int) -> bool:
        revs_number = 0
        y = x
        while(x > 0):
            revs_number = (revs_number * 10) + (x % 10)
            x = x // 10  
        if(y == revs_number):
            return True
        else:
            return False
    
